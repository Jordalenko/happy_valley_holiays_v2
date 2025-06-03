from . import views
from django.urls import path
from .views import HomePageView, ReviewList, review_detail


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('reviews/', ReviewList.as_view(), name='review_list'),
    path('reviews/<slug:slug>/', review_detail, name='review_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]
