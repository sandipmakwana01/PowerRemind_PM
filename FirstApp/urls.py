from django.urls import path
from FirstApp import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='home'),
    # Menu
    path('client_add/',views.client_add_view,name='client_add'),
    path('client_update/<int:id>',views.client_update_view,name='client_update'),
    path('client_delete/<int:id>',views.client_delete_view,name='client_delete'),
    # Authentication
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
