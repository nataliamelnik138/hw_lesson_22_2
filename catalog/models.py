from django.db import models
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    # created_at = models.DateField(verbose_name='Дата создания')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(**NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.CharField(max_length=10, verbose_name='Номер версии')
    name = models.CharField(max_length=150, verbose_name='Название версии')
    is_activ = models.BooleanField(verbose_name='Активная версия')

    def __str__(self):
        return f'{self.number} {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
