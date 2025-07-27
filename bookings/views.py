from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ReservationForm
from .models import Reservation
from cottages.models import Cottage
import json


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "bookings/reservation_form.html"
    success_url = reverse_lazy("home")  # adjust

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all booked date ranges for the selected cottage (or all if none selected)
        cottage_id = self.request.GET.get('cottage')
        if cottage_id:
            reservations = Reservation.objects.filter(cottage_id=cottage_id)
        else:
            reservations = Reservation.objects.all()
        booked_ranges = []
        for r in reservations:
            booked_ranges.append([
                r.check_in_date.strftime('%Y-%m-%d'),
                r.check_out_date.strftime('%Y-%m-%d')
            ])
        context['booked_ranges_json'] = json.dumps(booked_ranges)
        return context
    
    def get_initial(self):
        initial = super().get_initial()
        cottage_slug = self.request.GET.get("cottage")
        if cottage_slug:
            try:
                cottage = Cottage.objects.get(slug=cottage_slug)
                initial["cottage"] = cottage.pk
            except Cottage.DoesNotExist:
                pass
        return initial

    def form_valid(self, form):
        form.instance.guest = self.request.user
        # Set check_in_date and check_out_date from cleaned_data
        cleaned = form.cleaned_data
        form.instance.check_in_date = cleaned.get('check_in_date')
        form.instance.check_out_date = cleaned.get('check_out_date')
        return super().form_valid(form)