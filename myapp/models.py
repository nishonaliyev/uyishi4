from django.db import models
from django.utils import timezone

class Custom(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.CharField(max_length=30)
    yaroq_sana = models.DateTimeField()
    img = models.ImageField(upload_to='images', blank=True)

    def __str__(self) -> str:
        return self.nomi

