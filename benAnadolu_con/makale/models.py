from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Kategori(models.Model):
    isim = models.CharField(max_length = 50, null = True)
    slug = models.SlugField(max_length=50,unique=True,null=True)
    resim = models.ImageField(upload_to="kategori/%Y/%m/%d/", default="varsayilan.jpg")
    aciklama = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.isim

class Makale(models.Model):
    isim = models.CharField(max_length=200, unique=True, verbose_name="Makale Başlık")
    kategori = models.ForeignKey(Kategori, null=True, on_delete=models.DO_NOTHING)
    aciklama = RichTextUploadingField(blank=True, null=True)
    resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")
    tarih = models.DateTimeField(auto_now=True)
    erisim = models.BooleanField(default=True)
    basMakale = models.BooleanField(default=False)
    taliMakale = models.BooleanField(default=False)

    def __str__(self):
        return self.isim