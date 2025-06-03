from django.shortcuts import render
from django.views import generic
from .models import Cottage, Review

# Create your views here.
class CottageList(generic.ListView):
    queryset = Cottage.objects.all()
    template_name = "cottage_list.html"


class ReviewList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "cottage_list.html"
