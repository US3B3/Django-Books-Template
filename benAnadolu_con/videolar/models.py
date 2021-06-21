from django.db import models
from django.http.request import UploadHandlerList

class VideoDers(models.Model):
    ad = models.CharField(max_length=200, unique=True, verbose_name="Ders Başlığı", help_text="Video dersin başlığı..")
    aciklama = models.TextField(blank=True, null=True)
    resim = models.ImageField(upload_to="videolar/%Y/%m/%d/", default="varsayılan.jpg")
