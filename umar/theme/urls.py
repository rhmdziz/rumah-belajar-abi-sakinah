from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = "theme"

urlpatterns = [
    path("", index, name="index"),
    path('gallery/', galleryViews, name='gallery'),
    path('gallery/<int:id>', galleryViewsDetail, name='galleryDetail'),
    path('blog/<int:id>', blogViews, name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)