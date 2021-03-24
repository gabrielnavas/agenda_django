from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='accounts.index'),
  path('login', views.login, name='accounts.login'),
  path('logout', views.logout, name='accounts.logout'),
  path('signup', views.signup, name='accounts.signup'),
  path('dashboard', views.dashboard, name='accounts.dashboard'),
]