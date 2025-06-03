from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Cottage(models.Model):
    cottage_id = models.CharField(
        primary_key=True,
        max_length=20,
        default="Pen Y Graig"
    )
    # slug = models.SlugField(max_length=200, unique=True)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    max_guests = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cottage_id} Cottage"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    # rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Ratings from 1 to 5
    # title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Review by {self.guest} on {self.cottage}"

    # class Meta:
    #     unique_together = ('guest', 'cottage')
