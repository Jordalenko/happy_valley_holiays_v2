from django.db import models
# from cloudinary.models import CloudinaryField


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='about/images', blank=True,
                                      null=True, default='placeholder')
    content = models.TextField()

    def __str__(self):
        return self.title
