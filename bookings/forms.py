from django import forms
from .models import Reservation


class FlatpickrRangeInput(forms.TextInput):
    template_name = "widgets/flatpickr_range.html" 

    def __init__(self, **kwargs):
        kwargs.setdefault("attrs", {}).update({
            "placeholder": "Check‑in → Check‑out",
            "class": "form-control",
            "data-input": "",
            "data-inline": "true",  # This makes the calendar show inline
        })
        super().__init__(**kwargs)


class ReservationForm(forms.ModelForm):
    dates = forms.CharField(widget=FlatpickrRangeInput(), label="Dates")

    class Meta:
        model = Reservation
        fields = ["cottage", "dates", "guest_notes"]
        widgets = {
            'cottage': forms.HiddenInput()
        }

    def clean(self):
        cleaned = super().clean()
        # Split the range "YYYY‑MM‑DD to YYYY‑MM‑DD"
        if "dates" in cleaned and " to " in cleaned["dates"]:
            check_in, check_out = cleaned["dates"].split(" to ")
            cleaned["check_in_date"]  = check_in
            cleaned["check_out_date"] = check_out
        return cleaned
