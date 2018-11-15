from django.db import models


class BottomData(models.Model):

    title = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    color = models.CharField(max_length=512)
    sizes = models.CharField(max_length=512)
    specs = models.CharField(max_length=512)


class ExclusivesData(models.Model):

    title = models.CharField(max_length=512)
    price = models.CharField(max_length=512)

