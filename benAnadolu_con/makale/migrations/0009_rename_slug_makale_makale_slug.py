# Generated by Django 3.2.3 on 2021-08-16 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0008_makale_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makale',
            old_name='slug',
            new_name='makale_slug',
        ),
    ]
