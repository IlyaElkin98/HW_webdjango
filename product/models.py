from django.db import models

class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название",
        help_text="Введите название продукта",
    )

    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание",
    )

    price = models.IntegerField(
        verbose_name="Цена",
        help_text="Введите цену"
    )

    updated_at = models.DateField(
        verbose_name="Дата сохранения",
        auto_now=True,
    )

    publication_status = models.BooleanField(
        default=False,
        verbose_name='Статус публикации'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        permissions = [
            ('can_unpublish_product', 'Can unpublish product')
        ]

