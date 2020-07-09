from django.urls import path
from . import views

app_name = 'treasures'
urlpatterns = [
    path('', views.homeindex.as_view(), name='home'),
    path('<int:val>/', views.detail, name='detail'),
    path('add/', views.add_new, name='new_treasure'),
    path('<int:val>/edit/', views.edit_treasure, name='edit_treasure'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
