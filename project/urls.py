
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from machina.app import board
from productapp import views

urlpatterns = [
    path('', include('productapp.urls')),
    path('', include('hotel.urls')),
    path('admin/', admin.site.urls),
    path('forum/', include(board.urls)),


]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
