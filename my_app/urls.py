
from django.contrib import admin
from django.urls import path
from app_integracao_contabil import views

urlpatterns = [
    path('', views.integracao_contabil_view, name='integracao_contabil'),
    path('listagens/', views.listagens_execucao_view, name='listagens_execucao'),
]
