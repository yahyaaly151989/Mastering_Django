from django.urls import path
from. import views

urlpatterns = [
    path('create/', views.image_create, name='create')
]
