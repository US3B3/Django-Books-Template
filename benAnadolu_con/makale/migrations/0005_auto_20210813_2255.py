# Generated by Django 3.2.3 on 2021-08-13 22:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0004_auto_20210811_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='aciklama',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kategori',
            name='resim',
            field=models.ImageField(default='varsayilan.jpg', upload_to='kategori/%Y/%m/%d/'),
        ),
    ]
