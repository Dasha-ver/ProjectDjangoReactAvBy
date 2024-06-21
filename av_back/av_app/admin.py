from django.contrib import admin
from django_object_actions import DjangoObjectActions
from .models import GeneralPage, SecondPage, ThirdPage, Car, User, Rate
from .parser_for_rate import parser_for_rate


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']


class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'rate', 'date']


class GeneralPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count', 'link']


class SecondPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'mark', 'title', 'count', 'link']


class ThirdPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_name', 'link']


class CarAdmin(DjangoObjectActions, admin.ModelAdmin):
    def exchange(modeladmin, request, queryset):
        parser = parser_for_rate.ParserForRate()
        parser_for_rate.ParserForRate.run(parser)

    changelist_actions = ('exchange',)

    list_display = ['id', 'car', 'general_link', 'general_link_text', 'mark_link', 'mark_link_text', 'model_link',
                    'model_link_text', 'year', 'date_added', 'detailed_link', 'detailed_link_text',
                    'description_in_general',
                    'card_header', 'card_price_primary', 'card_price_secondary', 'card_commercial',
                    'card_params', 'card_short_description', 'card_short_modification', 'card_all_param_button_href',
                    'card_location', 'vin', 'image_links', 'card_comment_text', 'card_exchange', 'exterior',
                    'security_systems', 'pillows', 'help_systems', 'interior', 'comfort', 'heating', 'climate',
                    'multimedia', 'headlights', 'card_finance_image', 'card_finance_description',
                    'card_finance_item_subtitle', 'card_average_price', 'card_average_price_description',
                    'first_similar_ad_photo', 'first_similar_ad_link', 'first_similar_ad_title',
                    'first_similar_ad_price', 'first_similar_ad_params', 'second_similar_ad_photo',
                    'second_similar_ad_link', 'second_similar_ad_title', 'second_similar_ad_price',
                    'second_similar_ad_params', 'third_similar_ad_photo', 'third_similar_ad_link',
                    'third_similar_ad_title', 'third_similar_ad_price', 'third_similar_ad_params',
                    'fourth_similar_ad_photo', 'fourth_similar_ad_link', 'fourth_similar_ad_title',
                    'fourth_similar_ad_price', 'fourth_similar_ad_params', 'fifth_similar_ad_photo',
                    'fifth_similar_ad_link', 'fifth_similar_ad_title', 'fifth_similar_ad_price',
                    'fifth_similar_ad_params', 'sixth_similar_ad_photo', 'sixth_similar_ad_link',
                    'sixth_similar_ad_title', 'sixth_similar_ad_price', 'sixth_similar_ad_params',
                    'seventh_similar_ad_photo', 'seventh_similar_ad_link', 'seventh_similar_ad_title',
                    'seventh_similar_ad_price', 'seventh_similar_ad_params']


admin.site.register(GeneralPage, GeneralPageAdmin)
admin.site.register(SecondPage, SecondPageAdmin)
admin.site.register(ThirdPage, ThirdPageAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Rate, RateAdmin)
