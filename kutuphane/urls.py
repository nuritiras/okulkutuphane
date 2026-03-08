from django.urls import path
from . import views

urlpatterns = [
    path('', views.kitap_listesi, name='kitap_listesi'),
    path('ekle', views.kitap_ekle, name='kitap_ekle'),
    path('duzenle/<int:kitap_id>/', views.kitap_duzenle, name='kitap_duzenle'),
    path('kitap/sil/<int:kitap_id>/', views.kitap_sil, name='kitap_sil'),
]
