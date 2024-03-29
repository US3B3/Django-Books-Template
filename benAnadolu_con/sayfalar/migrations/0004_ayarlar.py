# Generated by Django 3.2.3 on 2021-09-03 18:50

import ckeditor.fields
import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0003_i̇letisim_okundu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ayarlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anasayfa_banner_baslik', models.CharField(max_length=50, unique=True, verbose_name='Anasayfa Başlık')),
                ('anasayfa_banner_aciklama', ckeditor.fields.RichTextField(blank=True)),
                ('anasayfa_banner_resim', models.ImageField(default='varsayilan.jpg', upload_to='makale/%Y/%m/%d/')),
                ('anasayfa_2seviye_baslik', models.CharField(max_length=50, unique=True, verbose_name='Anasayfa 2. Seviye Başlık')),
                ('anasayfa_2seviye_aciklama', ckeditor.fields.RichTextField(blank=True)),
                ('anasayfa_2seviye_resim', models.ImageField(default='varsayilan.jpg', upload_to='makale/%Y/%m/%d/')),
                ('anasayfa_video_baslik', models.CharField(max_length=50, unique=True, verbose_name='Anasayfa Videolar Başlık')),
                ('anasayfa_video_aciklama', models.TextField(blank=True, max_length=150)),
                ('anasayfa_4seviye_baslik', models.CharField(max_length=50, unique=True, verbose_name='Anasayfa 4. Seviye Başlık')),
                ('anasayfa_5seviye_baslik', models.CharField(max_length=50, unique=True, verbose_name='Anasayfa 5. Seviye Başlık')),
                ('anasayfa_6seviye_baslik', models.CharField(max_length=50, unique=True, verbose_name='Anasayfa 6. Seviye Başlık')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('ozel_renk', models.BooleanField(default=False)),
            ],
        ),
    ]
