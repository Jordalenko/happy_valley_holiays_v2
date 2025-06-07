from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Cottage, Review
from .forms import CommentForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = "cottages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cottage_list"] = Cottage.objects.all()
        return context


# def cottage_detail(request, slug):
#     queryset = Cottage.objects.filter(slug=slug)
#     cottage = get_object_or_404(queryset, slug=slug)
#     reviews = cottage.reviews.all().order_by("-created_on")
#     review_count = cottage.reviews.filter(approved=True).count()

def cottage_detail(request, slug):
    cottage = get_object_or_404(Cottage, slug=slug)
    images = cottage.images.all()
    cottages = Cottage.objects.all()
    reviews = cottage.reviews.all().order_by("-created_on")
    review_count = cottage.reviews.filter(approved=True).count()

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

    return render(request, 'cottages/cottage_detail.html', {
            'cottage': cottage,
            'cottages': cottages,
            'images': images,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": comment_form,
        }
    )

    # return render(
    #     request,
    #     "cottages/cottage_detail.html",
    #     {
    #         "cottage": cottage,
    #         "reviews": reviews,
    #         "review_count": review_count,
    #         "review_form": comment_form,
    #     }



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
