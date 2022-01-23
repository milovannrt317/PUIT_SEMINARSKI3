from django.urls import path
from . import views

app_name = 'prodavnicatrotineta'

urlpatterns = [path('', views.ListaTrotineta, name='ListaTrotineta'), path('<slug:segment_slug>/', views.ListaTrotineta, name='ListaTrotinetaPoSegmentu'), path('<int:id>/<slug:slug>/', views.DetaljiTrotineta, name='DetaljiTrotineta')]
