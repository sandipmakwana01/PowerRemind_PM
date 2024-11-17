from django.urls import path
from FirstApp import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='client'),
    # Menu
    path('profile/',views.profile,name='profile'),
    path('client_add/',views.client_add_view,name='client_add'),
    path('client_update/<int:id>',views.client_update_view,name='client_update'),
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
