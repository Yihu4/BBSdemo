from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('index', views.index, name='index'),
    path('reg', views.reg),
    path('word_list/', views.word_list),
    path('add_word/', views.add_word),
    url(r'^drop_word/', views.drop_word),

]
