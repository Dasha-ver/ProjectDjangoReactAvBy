from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Rate(models.Model):
    rate = models.FloatField(default=3.2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курсы валют'


class GeneralPage(models.Model):
    title = models.TextField(max_length=50, null=True)
    count = models.IntegerField()
    link = models.TextField(max_length=100)

    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Инфо главной страницы'
        verbose_name_plural = 'Инфо главной страницы'


class SecondPage(models.Model):
    mark = models.ForeignKey(GeneralPage, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=50, null=True)
    count = models.IntegerField()
    link = models.TextField(max_length=100)

    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Инфо второй страницы'
        verbose_name_plural = 'Инфо второй страницы'


class ThirdPage(models.Model):
    model_name = models.ForeignKey(SecondPage, on_delete=models.CASCADE, null=True)
    link = models.TextField(max_length=100)

    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return f'{self.model_name}'

    class Meta:
        verbose_name = 'Инфо третьей страницы'
        verbose_name_plural = 'Инфо третьей страницы'


class Car(models.Model):
    car = models.ForeignKey(ThirdPage, on_delete=models.CASCADE, null=True)
    general_link = models.TextField(max_length=300)
    general_link_text = models.TextField(max_length=300)
    mark_link = models.TextField(max_length=300)
    mark_link_text = models.TextField(max_length=300)
    model_link = models.TextField(max_length=300)
    model_link_text = models.TextField(max_length=300)
    year = models.IntegerField(default=1910)
    date_added = models.DateTimeField(auto_now_add=True)
    detailed_link = models.TextField(max_length=300)
    detailed_link_text = models.TextField(max_length=300)
    description_in_general = models.TextField(max_length=300)
    card_header = models.TextField(max_length=300)
    card_price_primary = models.IntegerField()
    card_price_secondary = models.IntegerField()
    card_commercial = models.TextField(max_length=300)
    card_params = models.TextField(max_length=400)
    card_short_description = models.TextField(max_length=500)
    card_short_modification = models.TextField(max_length=500)
    card_all_param_button_href = models.TextField(max_length=300)
    card_location = models.TextField(max_length=300)
    vin = models.TextField(max_length=100)
    image_links = models.TextField(max_length=1000)
    card_comment_text = models.TextField(max_length=10000)
    card_exchange = models.TextField(max_length=500)
    exterior = models.TextField(max_length=1000)
    security_systems = models.TextField(max_length=1000)
    pillows = models.TextField(max_length=500)
    help_systems = models.TextField(max_length=1000)
    interior = models.TextField(max_length=1000)
    comfort = models.TextField(max_length=1000)
    heating = models.TextField(max_length=500)
    climate = models.TextField(max_length=500)
    multimedia = models.TextField(max_length=1000)
    headlights = models.TextField(max_length=500)
    card_finance_image = models.TextField(max_length=300)
    card_finance_description = models.TextField(max_length=300)
    card_finance_item_subtitle = models.TextField(max_length=300)
    card_average_price = models.TextField(max_length=100)
    card_average_price_description = models.TextField(max_length=500)
    first_similar_ad_photo = models.TextField(max_length=300)
    first_similar_ad_link = models.TextField(max_length=300)
    first_similar_ad_title = models.TextField(max_length=300)
    first_similar_ad_price = models.TextField(max_length=300)
    first_similar_ad_params = models.TextField(max_length=300)
    second_similar_ad_photo = models.TextField(max_length=300)
    second_similar_ad_link = models.TextField(max_length=300)
    second_similar_ad_title = models.TextField(max_length=300)
    second_similar_ad_price = models.TextField(max_length=300)
    second_similar_ad_params = models.TextField(max_length=300)
    third_similar_ad_photo = models.TextField(max_length=300)
    third_similar_ad_link = models.TextField(max_length=300)
    third_similar_ad_title = models.TextField(max_length=300)
    third_similar_ad_price = models.TextField(max_length=300)
    third_similar_ad_params = models.TextField(max_length=300)
    fourth_similar_ad_photo = models.TextField(max_length=300)
    fourth_similar_ad_link = models.TextField(max_length=300)
    fourth_similar_ad_title = models.TextField(max_length=300)
    fourth_similar_ad_price = models.TextField(max_length=300)
    fourth_similar_ad_params = models.TextField(max_length=300)
    fifth_similar_ad_photo = models.TextField(max_length=300)
    fifth_similar_ad_link = models.TextField(max_length=300)
    fifth_similar_ad_title = models.TextField(max_length=300)
    fifth_similar_ad_price = models.TextField(max_length=300)
    fifth_similar_ad_params = models.TextField(max_length=300)
    sixth_similar_ad_photo = models.TextField(max_length=300)
    sixth_similar_ad_link = models.TextField(max_length=300)
    sixth_similar_ad_title = models.TextField(max_length=300)
    sixth_similar_ad_price = models.TextField(max_length=300)
    sixth_similar_ad_params = models.TextField(max_length=300)
    seventh_similar_ad_photo = models.TextField(max_length=300)
    seventh_similar_ad_link = models.TextField(max_length=300)
    seventh_similar_ad_title = models.TextField(max_length=300)
    seventh_similar_ad_price = models.TextField(max_length=300)
    seventh_similar_ad_params = models.TextField(max_length=300)
    bookmakers = models.ManyToManyField(User, through='UserCarRelation')

    def __str__(self):
        return f'{self.card_header}'

    class Meta:
        verbose_name = 'Карточка авто'
        verbose_name_plural = 'Карточки авто'


class UserCarRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        ordering = ['-id']
