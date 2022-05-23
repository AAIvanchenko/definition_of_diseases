from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('result', views.result, name='result'),
    path('guide', views.guide, name='guide'),
    path('upload', views.file_upload, name='upload-file')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
