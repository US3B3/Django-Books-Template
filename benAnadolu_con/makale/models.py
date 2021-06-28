from django.db import models
from ckeditor.fields import RichTextField

class Makale(models.Model):
    isim = models.CharField(max_length=200, unique=True, verbose_name="Makale Başlık")
    aciklama = RichTextField(blank=True, null=True)
    resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")
    tarih = models.DateTimeField(auto_now=True)
    erisim = models.BooleanField(default=True)

    def __str__(self):
        return self.isim