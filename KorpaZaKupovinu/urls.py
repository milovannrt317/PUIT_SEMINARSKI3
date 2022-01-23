from django.urls import path
from . import views

app_name = 'korpazakupovinu'

urlpatterns = [
    path('', views.DetaljiKorpe, name='DetaljiKorpe'),
    path('dodaj/<int:trotinet_id>/',
         views.DodajUKorpu, name='DodajUKorpu'),
    path('ukloni/<int:trotinet_id>/',
         views.UkloniIzKorpe, name='UkloniIzKorpe'),
]
