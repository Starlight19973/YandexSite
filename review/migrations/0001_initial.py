# Generated by Django 4.2.7 on 2023-11-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('review_body', models.TextField(verbose_name='Текст обзора')),
                ('pros', models.TextField(blank=True, null=True, verbose_name='Плюсы')),
                ('cons', models.TextField(blank=True, null=True, verbose_name='Минусы')),
                ('purchase_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на обзор')),
                ('review_date', models.DateTimeField(verbose_name='Дата обзора')),
            ],
            options={
                'verbose_name': 'Обзор бытовой техники',
                'verbose_name_plural': 'Обзоры бытовой техники',
            },
        ),
    ]
