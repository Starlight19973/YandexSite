from django.db import models


class Review(models.Model):
    product_name = models.CharField('Название продукта', max_length=100)
    model = models.CharField('Модель', max_length=50)
    review_body = models.TextField('Текст обзора')
    pros = models.TextField('Плюсы', null=True, blank=True)
    cons = models.TextField('Минусы', null=True, blank=True)
    purchase_link = models.URLField('Ссылка на обзор', max_length=200, blank=True, null=True)
    review_date = models.DateTimeField('Дата обзора')

    def __str__(self):
        return f"{self.product_name} - {self.model}"

    class Meta:
        verbose_name = 'Обзор бытовой техники'
        verbose_name_plural = 'Обзоры бытовой техники'
