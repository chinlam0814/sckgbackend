from django.urls import path
from . import views

urlpatterns = [
    path('', views.files_list),
    path('<int:pk>/', views.file_info),
    path('<int:pk>/file/', views.file),
    path('create/info/', views.create_file_info),
    path('create/<int:pk>/file/', views.create_file),
    path('<int:pk>/delete/', views.delete_file),
    path('extract/file/', views.extract_text_from_pdf),
]
