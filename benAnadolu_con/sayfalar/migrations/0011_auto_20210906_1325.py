# Generated by Django 3.2.3 on 2021-09-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0010_ayarlar_anasayfa_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayarlar',
            name='meta_anasayfa_description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='ayarlar',
            name='meta_anasayfa_keywords',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
