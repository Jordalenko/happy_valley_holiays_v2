from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Cottage, Review

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
    return render(
        request,
        "cottages/review_detail.html",
        {"review": review},
    )
