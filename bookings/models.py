from django.db import models
from django.contrib.auth.models import User
from guest_profile.models import Guest
from cottages.models import Cottage

STATUS = ((0, "Draft"), (1, "Published"))


class Reservation(models.Model):
    res_id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    is_completed = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    guest_notes = models.TextField(blank=True, null=True, max_length=300)
    host_notes = models.TextField(blank=True, null=True, max_length=1000)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Reservation {self.res_id} by {self.guest}"

    class Meta:
        ordering = ["-created_at"]
