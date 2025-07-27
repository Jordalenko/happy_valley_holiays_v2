from django.urls import path
from .views import ReservationCreateView

app_name = "bookings"

urlpatterns = [
    path(
        "new/",
        ReservationCreateView.as_view(),
        name="reservation_new"
    ),
]
