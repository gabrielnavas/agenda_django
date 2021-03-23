from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='contacts.index'),
  path('<int:contact_id>', views.show_contact, name='contacts.show_contact'),
  path('search/', views.search, name='contacts.search'),
]