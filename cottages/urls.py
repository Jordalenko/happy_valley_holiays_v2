from django.urls import path
from .views import (
    HomePageView,
    cottage_detail,
    review_edit,
    review_delete,
    review_detail,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('reviews/', review_detail, name='review_detail'),
    path('<slug:slug>/', cottage_detail, name='cottage_detail'),
    path('<slug:slug>/edit_review/<slug:review_slug>/',
         review_edit,
         name='review_edit'),
    path('<slug:slug>/delete_review/<slug:review_slug>/',
         review_delete,
         name='review_delete'),
]
