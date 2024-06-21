from django.urls import path
from . import views

urlpatterns = [
    path('', views.texts_list),
    path('<int:pk>/', views.text),
    path('create/', views.create_text),
    #path('graph/', views.generate_text),
    path('<int:textId>/delete/', views.delete_text)
]
