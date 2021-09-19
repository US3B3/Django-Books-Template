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
    anasayfa_logo = models.CharField(max_length=50, unique=True, verbose_name="Logo İsim",blank=True)

    anasayfa_banner_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa Başlık",blank=True)
    anasayfa_banner_aciklama = RichTextField(blank=True)

    anasayfa_banner_baslik2 = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa Başlık",blank=True)
    anasayfa_banner_aciklama2 = RichTextField(blank=True)

    anasayfa_banner_resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")

    anasayfa_2seviye_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa 2. Seviye Başlık",blank=True)
    anasayfa_2seviye_aciklama = RichTextField(blank=True)
    anasayfa_2seviye_resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")

    anasayfa_video_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa Videolar Başlık",blank=True)
    anasayfa_video_aciklama = models.TextField(max_length=150 ,blank=True)
    anasayfa_video_resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")

    anasayfa_4seviye_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa 4. Seviye Başlık",blank=True)

    anasayfa_5seviye_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa 5. Seviye Başlık",blank=True)

    anasayfa_6seviye_baslik = models.CharField(max_length=50, unique=True, verbose_name="Anasayfa 6. Seviye Başlık",blank=True)

    color = ColorField(default='#0e3746')
    ozel_renk = models.BooleanField(default=False)

    footer_aciklama_baslik = models.CharField(max_length=25, unique=True, verbose_name="Footer açıklama başlık", blank=True)
    footer_aciklama = models.TextField(max_length=150, blank=True)
    footer_facebook = models.URLField(unique=True, null=True)
    footer_twitter = models.URLField(unique=True, null=True)
    footer_youtube = models.URLField(unique=True, null=True)
    footer_instagram = models.URLField(unique=True, null=True)

    footer_iletisim_baslik = models.CharField(max_length=25, unique=True, verbose_name="İletişim başlık", blank=True)
    footer_iletisim_aciklama = RichTextField(blank=True)
    footer_iletisim_konum = models.CharField(max_length=50, verbose_name="Adres",blank=True)
    footer_iletisim_tel = models.CharField(max_length=20, verbose_name="Telefon numarası", blank=True)
    footer_iletisim_mail = models.CharField(max_length=50, verbose_name="Mail", blank=True)

    footer_mail_baslik = models.CharField(max_length=50, verbose_name="Mail başlık", blank=True)

    meta_anasayfa_keywords = models.TextField(blank=True, null=True)
    meta_anasayfa_description = models.TextField(max_length=250, blank=True)

    blog_gorunurluk = models.BooleanField(blank=True, default=True)
    blogMakale_gorunurluk = models.BooleanField(blank=True, default=True)
    blogKategori_gorunurluk = models.BooleanField(blank=True, default=True)
    video_gorunurluk = models.BooleanField(blank=True, default=True)
    galeri_gorunurluk = models.BooleanField(blank=True, default=True)
    vitrin_gorunurluk = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.anasayfa_banner_baslik