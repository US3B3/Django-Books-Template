# Generated by Django 3.2.3 on 2021-08-31 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrin', '0002_vitrin_yazar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitrin',
            name='yazar',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Yazar'),
        ),
    ]
