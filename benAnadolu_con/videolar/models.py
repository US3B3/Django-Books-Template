from django.db import models

class VideoDers(models.Model):
    isim = models.CharField(max_length=200, unique=True, verbose_name="Ders Başlığı", help_text="Video dersin başlığı..")
    aciklama = models.TextField(blank=True, null=True)
    resim = models.ImageField(upload_to="videolar/%Y/%m/%d/", default="varsayilan.jpg")
    tarih = models.DateTimeField(auto_now=True)
    erisim = models.BooleanField(default=True)

    def __str__(self):
        return self.isim
