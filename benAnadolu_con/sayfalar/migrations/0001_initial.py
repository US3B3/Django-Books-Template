# Generated by Django 3.2.3 on 2021-09-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='İletisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adsoyad', models.CharField(max_length=100)),
                ('numara', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('mesaj', models.TextField(blank=True)),
            ],
        ),
    ]
