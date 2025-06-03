from . import views
from django.urls import path


urlpatterns = [
    path('', views.CottageList.as_view(), name='home'),
]
