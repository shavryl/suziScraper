from django.db import models


class BottomData(models.Model):
    """
    The scrapped data will be saved in this model
    """
    title = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    color = models.CharField(max_length=512)
    sizes = models.CharField(max_length=512)
