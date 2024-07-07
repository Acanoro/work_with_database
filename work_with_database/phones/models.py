import uuid

from django.core.validators import MinValueValidator
from django.db import models


def phone_cover_image_path(instance, filename):
    image_path = f'phones/{instance.name}/cover_image/{uuid.uuid4}.jpg'

    return image_path


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название телефона')
    price = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Цена'
    )
    image = models.ImageField(upload_to=phone_cover_image_path, verbose_name='Обложка телефона')
    release_date = models.DateField(verbose_name='release_date')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефон'
