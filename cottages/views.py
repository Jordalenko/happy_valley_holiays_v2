from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Cottage, Review
from .forms import CommentForm
import os
from .forms import ReviewForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
class HomePageView(TemplateView):
    template_name = "cottages/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["cottage_list"] = Cottage.objects.all()
        context["review_list"] = Review.objects.all()

        review_qs = Review.objects.filter(approved=True).order_by('-rating', '-created_at')
        paginator = Paginator(review_qs, 3)

        page = self.request.GET.get("page")
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context["review_list"] = page_obj.object_list
        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()

        lake_images = []  # Always define it first

        lake_folder = os.path.join(settings.MEDIA_ROOT, 'hero')
        if os.path.exists(lake_folder):
            lake_images = [
                f"hero/{img}"
                for img in os.listdir(lake_folder)
                if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
            ]

        for img in lake_images:
            full_path = os.path.join(settings.MEDIA_ROOT, img)
            print(f"Checking: {full_path} --> Exists: {os.path.exists(full_path)}")

        context["lake_images"] = lake_images
        
        return context


def cottage_detail(request, slug):
    cottage = get_object_or_404(Cottage, slug=slug)
    images = cottage.images.all()
    cottages = Cottage.objects.all()

    review_qs = Review.objects.filter(approved=True).order_by('-rating', '-created_at')
    paginator = Paginator(review_qs, 3)

    page = self.request.GET.get("page")
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    # Filter and order reviews
    reviews_qs = cottage.reviews.filter(approved=True).order_by("-created_on")
    review_count = reviews_qs.count()

    # Set up pagination
    paginator = Paginator(reviews_qs, 1)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    # Handle comment form
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, files=request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.guest = request.user
            comment.cottage = cottage
            comment.save()
            messages.success(request, 'Review submitted and awaiting approval')
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()

    context = {
        'cottage': cottage,
        'cottages': cottages,
        'images': images,
        'reviews': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'review_count': review_count,
        'review_form': comment_form,
    }

    return render(request, 'cottages/cottage_detail.html', context)


def review_detail(request):
    cottages = ['rock-terrace', 'pen-y-graig']
    paginated_reviews_by_cottage = {}

    for slug in cottages:
        cottage = get_object_or_404(Cottage, slug=slug)
        reviews_qs = Review.objects.filter(cottage=cottage, approved=True).order_by('-rating', '-created_at')
        paginator = Paginator(reviews_qs, 3)
        page_number = request.GET.get(f'page_{slug}')
        page_obj = paginator.get_page(page_number)
        paginated_reviews_by_cottage[cottage] = page_obj

    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.guest = request.user
            review.save()
            messages.success(request, 'Review submitted and awaiting approval.')
            return HttpResponseRedirect(request.path_info)
    else:
        review_form = ReviewForm()

    return render(request, 'cottages/review_detail.html', {
        'paginated_reviews_by_cottage': paginated_reviews_by_cottage,
        'review_form': review_form,
    })


def review_edit(request, slug, review_id):
    cottage = get_object_or_404(Cottage, slug=slug)
    review = get_object_or_404(Review, id=review_id, guest=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('cottage_detail', slug=slug)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'review_edit.html', {'form': form})


def review_delete(request, slug, review_id):
    cottage = get_object_or_404(Cottage, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You can only delete your own review!')

    return HttpResponseRedirect(reverse('cottage_detail', args=[slug]))
