from . import views
from django.urls import path


urlpatterns = [
    path('', views.CottageList.as_view(), name='home'),
    path('<slug:slug>/', views.review_detail, name='review_detail'),
]
