from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class VideoGame(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=3000)
    listing_posted = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)


