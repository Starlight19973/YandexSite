# Generated by Django 5.0 on 2023-12-07 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0006_delete_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
