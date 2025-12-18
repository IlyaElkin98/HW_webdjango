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
        max_length=30,
        help_text="Введите цену"
    )

    updated_at = models.DateField(
        verbose_name="Дата сохранения",
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
