from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nick', views.nick, name='nick'),
    path('helen', views.helen, name='helen'),
    path('<str:name>', views.greet, name='greet'),
]
