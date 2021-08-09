# Generated by Django 3.2.3 on 2021-08-09 09:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0002_auto_20210625_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='makale',
            name='basMakale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='makale',
            name='taliMakale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='makale',
            name='aciklama',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='makale',
            name='isim',
            field=models.CharField(max_length=200, unique=True, verbose_name='Makale Başlık'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='resim',
            field=models.ImageField(default='varsayilan.jpg', upload_to='makale/%Y/%m/%d/'),
        ),
    ]
