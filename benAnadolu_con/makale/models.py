from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Makale(models.Model):
    isim = models.CharField(max_length=200, unique=True, verbose_name="Makale Başlık")
    aciklama = RichTextUploadingField(blank=True, null=True)
    resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")
    tarih = models.DateTimeField(auto_now=True)
    erisim = models.BooleanField(default=True)
    basMakale = models.BooleanField(default=False)
    taliMakale = models.BooleanField(default=False)

    def __str__(self):
        return self.isim