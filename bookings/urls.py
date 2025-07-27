from django.urls import path
from .views import ReservationCreateView

urlpatterns = [
    path(
        "new/",
        ReservationCreateView.as_view(),
        name="reservation_new"
    ),
]
