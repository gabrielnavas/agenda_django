from django.contrib import admin
from .models import Category, Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'last_name', 'phone', 'email', 'created_at', 'description', 'category')

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
