from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

class İletisim(models.Model):
    ad_soyad = models.CharField(max_length=100)
    numara = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    mesaj = models.TextField(blank=True)
    okundu = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Ayarlar(models.Model):
    anasayfa_banner_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa Başlık",blank=True)
    anasayfa_banner_aciklama = RichTextField(blank=True)
    anasayfa_banner_resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")

    anasayfa_2seviye_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa 2. Seviye Başlık",blank=True)
    anasayfa_2seviye_aciklama = RichTextField(blank=True)
    anasayfa_2seviye_resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")

    anasayfa_video_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa Videolar Başlık",blank=True)
    anasayfa_video_aciklama = models.TextField(max_length=150 ,blank=True)

    anasayfa_4seviye_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa 4. Seviye Başlık",blank=True)

    anasayfa_5seviye_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa 5. Seviye Başlık",blank=True)

    anasayfa_6seviye_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa 6. Seviye Başlık",blank=True)

    color = ColorField(default='#FF0000')
    ozel_renk = models.BooleanField(default=False)

    def __str__(self):
        return self.anasayfa_banner_baslik