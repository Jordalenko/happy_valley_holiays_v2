import os
from .models import Cottage, Review, HeroImage
from .forms import ReviewForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.db.models import Q


# home page view
class HomePageView(TemplateView):
    template_name = "cottages/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["cottage_list"] = Cottage.objects.all()
        context["review_list"] = Review.objects.all()

        # Filter and order reviews
        review_qs = Review.objects.filter(
            approved=True
        ).order_by(
            '-rating', '-created_at'
        )
        paginator = Paginator(review_qs, 3)

        # Handle pagination
        page = self.request.GET.get("page")
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        # Add paginated reviews to context
        context["review_list"] = page_obj.object_list
        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()

        context["lake_images"] = HeroImage.objects.filter(image__isnull=False).exclude(image='').order_by('image')

        return context


# Cottage detail view
def cottage_detail(request, slug):
    cottage = get_object_or_404(Cottage, slug=slug)
    images = cottage.images.all().order_by('image')
    cottages = Cottage.objects.all()

    # Filter and order reviews
    reviews_qs = cottage.reviews.filter(
        approved=True
    ).order_by("-created_on")
    review_count = reviews_qs.count()

    # Set up pagination
    paginator = Paginator(reviews_qs, 1)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    # Handle review form
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, files=request.FILES)
        if review_form.is_valid():
            review = review_form.save(
                commit=False
            )
            review.guest = request.user
            review.cottage = cottage
            review.save()

    else:
        review_form = ReviewForm()

    context = {
        'cottage': cottage,
        'cottages': cottages,
        'images': images,
        'reviews': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'review_count': review_count,
        'review_form': review_form,
    }

    return render(request, 'cottages/cottage_detail.html', context)


# Review detail view
def review_detail(request):
    cottages = ['rock-terrace', 'pen-y-graig']
    paginated_reviews_by_cottage = {}
    # Get all cottages to paginate reviews
    for slug in cottages:
        cottage = get_object_or_404(Cottage, slug=slug)
        reviews_qs = (
            Review.objects.filter(cottage=cottage, approved=True)
            .order_by('-rating', '-created_at')
        )
        paginator = Paginator(reviews_qs, 3)
        page_number = request.GET.get(f'page_{slug}')
        page_obj = paginator.get_page(page_number)
        paginated_reviews_by_cottage[cottage] = page_obj
    # Handle review submission
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.guest = request.user
            review.save()
            messages.success(
                request,
                'Review submitted and awaiting approval.'
            )
            return HttpResponseRedirect(request.path_info)
    else:
        review_form = ReviewForm()
    # Render the template with paginated reviews and review form
    return render(request, 'cottages/review_detail.html', {
        'paginated_reviews_by_cottage': paginated_reviews_by_cottage,
        'review_form': review_form,
    })


# Review edit and delete views
def review_edit(request, slug, review_slug):
    review = get_object_or_404(Review, slug=review_slug, guest=request.user)
    # Handle review submission
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.approved = False  # Reset approval on edit
            review.save()
            messages.info(
                request,
                "Your edited review is now awaiting approval."
            )
            return redirect('cottage_detail', slug=slug)
    else:
        form = ReviewForm(instance=review)
    # Render the edit form
    return render(request, 'review_edit.html', {'form': form})


# Review delete view
def review_delete(request, slug, review_slug):
    review = get_object_or_404(Review, slug=review_slug, cottage__slug=slug)
    # Check if the user is the guest who wrote the review
    if review.guest == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You can only delete your own review!')
    # Redirect to the cottage detail page
    return HttpResponseRedirect(reverse('cottage_detail', args=[slug]))
