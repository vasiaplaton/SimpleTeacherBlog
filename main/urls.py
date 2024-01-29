from django.urls import path
from . import views

# добавляем переходы на нужные страницы
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('results/', views.results, name='results'),
    path("register", views.register_request, name="register")
]
