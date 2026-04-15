from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apresentacao/', views.apresentacao, name='apresentacao'),
    path('resumo/', views.resumo, name='resumo'),
    path('sobre/', views.sobre, name='sobre'),
    path('libras/', views.libras, name='libras'),
    path('rcpd/', views.rcpd, name='rcpd'),
    path('normativa/', views.normativa, name='normativa'),
    path('funcionalidades/', views.funcionalidades, name='funcionalidades'),
    path('exercicios/', views.exercicios, name='exercicios'),
    path('exercicios/iniciante/', views.exercicios_iniciante, name='exercicios_iniciante'),
    path('exercicios/medio/', views.exercicios_medio, name='exercicios_medio'),
    path('exercicios/avancado/', views.exercicios_avancado, name='exercicios_avancado'),
    path('acessibilidade/', views.acessibilidade, name='acessibilidade'),
    path('lembretes/', views.lembretes, name='lembretes'),
    path('acompanhamento/', views.acompanhamento, name='acompanhamento'),
    path('publico-alvo/', views.publico_alvo, name='publico_alvo'),
    path('deficiencias/', views.deficiencias, name='deficiencias'),
    path('cuidadores/', views.cuidadores, name='cuidadores'),
    path('beneficios/', views.beneficios, name='beneficios'),
    path('impactos/', views.impactos, name='impactos'),
    path('contato/', views.contato, name='contato'),
]
