from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('panel/', views.admin_panel, name='admin_panel'),
    path('panel/users/add/', views.admin_user_create, name='admin_user_create'),
    path('panel/users/<int:pk>/delete/', views.admin_user_delete, name='admin_user_delete'),
]
