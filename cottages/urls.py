from . import views
from django.urls import path
from .views import HomePageView, ReviewList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('reviews/', ReviewList.as_view(), name='review_list'),
    path('<slug:slug>/', review_detail, name='review_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
