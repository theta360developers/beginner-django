from django.db import models


class Thetaimage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=160)

    def __str__(self):
        return self.title
