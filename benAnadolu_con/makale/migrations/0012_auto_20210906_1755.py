# Generated by Django 3.2.3 on 2021-09-06 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0011_remove_kategori_meta_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makale',
            name='etiketler',
        ),
        migrations.AddField(
            model_name='makale',
            name='etiketler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='makale.etiket'),
        ),
    ]
