from . import views
from django.urls import path
from .views import ReservationCreateView

app_name = "bookings"

urlpatterns = [
    path(
        "new/",
        ReservationCreateView.as_view(),
        name="reservation_new"
    ),
    path("booked-dates/<slug:cottage_slug>/",
         views.booked_dates_json,
         name="booked_dates_json")
]
