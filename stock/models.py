from django.db import models


class Goods(models.Model):
    appearance = models.ImageField('Изображение товара', upload_to='images/')
    title = models.CharField('Название товара', max_length=100)
    details = models.TextField('Описание товара')
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=2)

    def __str(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
