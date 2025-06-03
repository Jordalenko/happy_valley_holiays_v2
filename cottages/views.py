from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Cottage, Review, Comment
from .forms import CommentForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = "cottages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cottage_list"] = Cottage.objects.all()
        context["review_list"] = (
            Review.objects.filter(status=1)
            .order_by('-created_at')[:6]
        )
        return context


class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "reviews/index.html"
    paginate_by = 3


def review_detail(request, slug):
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
        )

    comment_form = CommentForm()

    print("About to render template")

    return render(
        request,
        "cottages/review_detail.html",
        {"review": review},
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comment
    """
    if request.method == "POST":

        queryset = Comment.objects.filter(status=1)
        comment = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment = comment
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    queryset = comment.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Review, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comment!')

    return HttpResponseRedirect(reverse('comment_detail', args=[slug]))
