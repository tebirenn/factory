from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),

        # Подключение URL адресов приложении
    path('authorize/', include('authorize.urls')),
]

        # Подключение URL для доступа к медиа файлам
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)