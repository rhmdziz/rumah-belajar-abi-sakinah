from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = "theme"

urlpatterns = [
    path("", index, name="index"),
    path('gallery/', galleryView, name='gallery'),
    path('blog/<int:id>', blogViews, name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)