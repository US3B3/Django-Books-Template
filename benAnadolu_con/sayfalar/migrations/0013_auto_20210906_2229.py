# Generated by Django 3.2.3 on 2021-09-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0012_alter_ayarlar_meta_anasayfa_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayarlar',
            name='blogKategori_gorunurluk',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='ayarlar',
            name='blogMakale_gorunurluk',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='ayarlar',
            name='blog_gorunurluk',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='ayarlar',
            name='galeri_gorunurluk',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='ayarlar',
            name='video_gorunurluk',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='ayarlar',
            name='vitrin_gorunurluk',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
