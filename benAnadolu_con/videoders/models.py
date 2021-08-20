from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class VideoDers(models.Model):
    videobaslik = models.CharField(max_length=100, unique=True, verbose_name="Video Başlık", null=True)
    videoaciklama = RichTextUploadingField(blank=True, null=True)
    videourl = models.URLField(max_length=100, null=True)
    erisim = models.BooleanField(default=True)
    tarih = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.videobaslik
