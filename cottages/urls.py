from . import views
from django.urls import path
from .views import HomePageView, ReviewList, review_detail


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('reviews/', ReviewList.as_view(), name='review_list'),
    path('reviews/<slug:slug>/', review_detail, name='review_detail'),
]
