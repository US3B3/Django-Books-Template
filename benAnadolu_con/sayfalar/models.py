from django.db import models

class İletisim(models.Model):
    ad_soyad = models.CharField(max_length=100)
    numara = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    mesaj = models.TextField(blank=True)

    def __str__(self):
        return self.email
