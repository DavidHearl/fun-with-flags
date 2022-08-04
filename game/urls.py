from django.urls import path
from . import views

urlpatterns = [
    path('', views.game, name='game'),
    path('easy/', views.game, name='easy'),
    path('medium/', views.game, name='medium'),
    path('hard/', views.game, name='hard'),
    path('extreme/', views.game, name='extreme')
]