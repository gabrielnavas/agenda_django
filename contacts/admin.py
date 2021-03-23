from django.contrib import admin
from .models import Category, Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'last_name', 'phone', 'email', 'created_at', 'description', 'category', 'is_show')
  list_display_links = ('id', 'name', 'last_name')
  list_per_page = 3
  search_fields = ('name', 'last_name', 'email')
  list_editable = ('phone', 'is_show')

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)



