from django.urls import path
from .views import MapView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', MapView.as_view(), name='map'),
    path('driver/', views.driver, name='driver'),   
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
