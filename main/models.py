from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    comment = models.TextField()

    def __str__(self):
        return f"{self.first_name}"


class BannerImg(models.Model):
    photo = models.ImageField(upload_to="static/images/")

    def __str__(self) -> str:
        return self.photo
