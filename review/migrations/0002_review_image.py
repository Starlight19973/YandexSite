# Generated by Django 5.0 on 2023-12-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles_images/', verbose_name='Фотография товара'),
        ),
    ]