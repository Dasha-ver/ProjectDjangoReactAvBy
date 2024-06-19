from django.contrib import admin
from .models import GeneralPage, SecondPage, ThirdPage, Car, User
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.http import HttpResponse, JsonResponse
from django.contrib import admin
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt


class MyModelModelAdmin(ExtraButtonsMixin, admin.ModelAdmin):

    @button(permission='demo.add_demomodel1',
            visible=lambda self: self.context["request"].user.is_superuser,
            change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def refresh(self, request):
        self.message_user(request, 'refresh called')
        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)

    @button(html_attrs={'style': 'background-color:#DC6C6C;color:black'})
    def confirm(self, request):
        def _action(request):
            pass

        return confirm_action(self, request, _action, "Confirm action",
                              "Successfully executed", )

    @link(href=None,
          change_list=False,
          html_attrs={'target': '_new', 'style': 'background-color:var(--button-bg)'})
    def search_on_google(self, button):
        original = button.context['original']
        button.label = f"Search '{original.name}' on Google"
        button.href = f"https://www.google.com/?q={original.name}"

    @view()
    def select2_autocomplete(self, request):
        return JsonResponse({})

    @view(http_basic_auth=True)
    def api4(self, request):
        return HttpResponse("Basic Authentication allowed")

    @view(decorators=[csrf_exempt, xframe_options_sameorigin])
    def preview(self, request):
        if request.method == "POST":
            return HttpResponse("POST")
        return HttpResponse("GET")


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']


class GeneralPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count', 'link']


class SecondPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'mark', 'title', 'count', 'link']


class ThirdPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_name', 'link']


class CarAdmin(admin.ModelAdmin):
    change_form_template = 'av_back/av_app/templates/admin/my_change_form.html'
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
