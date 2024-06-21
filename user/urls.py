from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('logout/', views.user_logout),

    path('account/', views.accounts_list),
    path('admin/', views.admins_list),

    path('account/<int:pk>/', views.account),
    path('admin/<int:pk>/', views.admin),

    path('account/create/', views.create_account),
    path('admin/create/', views.create_admin),
    
    path('account/<int:pk>/delete/', views.delete_account),
    path('admin/<int:pk>/delete/', views.delete_admin),
    path('account/<int:pk>/change/', views.account_change_password),
    path('admin/<int:pk>/change/', views.admin_change_password),

    path('<int:pk>/edit/username/', views.edit_username),
    path('<int:pk>/edit/gender/', views.edit_gender),
]
