from django.contrib import admin
from .models import Category, Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'last_name', 'phone', 'email', 'created_at', 'description', 'category')
  list_display_links = ('id', 'name', 'last_name')
  list_filter = ('name', 'email')
  list_per_page = 3
  search_fields = ('name', 'last_name', 'email')


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
