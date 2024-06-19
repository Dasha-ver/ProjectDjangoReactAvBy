from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('admin/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('admin/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('', include('av_app.urls')),
    path('swagger/', get_swagger_view(title='Av API')),
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
