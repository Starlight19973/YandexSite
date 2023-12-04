from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Article(models.Model):
    image = models.ImageField('Фотография товара', upload_to='articles_images/', null=True, blank=True)
    title = models.CharField('Название', max_length=100)
    full_text = models.TextField('Полное описание')
    rating = models.FloatField(
        'Рейтинг',
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        default=0.0
    )
    review = models.TextField('Отзыв', null=True, blank=True)
    date = models.DateTimeField('Дата публикации')
    purchase_link = models.URLField('Ссылка на покупку', max_length=200, blank=True, null=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


