from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Cottage, Review

# Create your views here.
class CottageList(generic.ListView):
    queryset = Cottage.objects.all()
    template_name = "cottages/index.html"
paginate_by = 2


def review_detail(request, slug):
    """
    Display an individual :model:`review.Post`.

    **Context**

    ``post``
        An instance of :model:`review.Post`.

    **Template:**

    :template:`cottages/review_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "cottages/review_detail.html",
        {"review": Review},
    )

class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "reviews/index.html"
paginate_by = 3
