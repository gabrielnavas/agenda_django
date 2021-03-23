from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from .models import Contact

def index(request):
  contacts = Contact.objects.all()
  paginator = Paginator(contacts, 3)
  page=request.GET.get('p')
  contacts_paginator = paginator.get_page(page)
  return render(request, 'contacts/index.html', {
    'contacts': contacts_paginator
  })


def show_contact(request, contact_id):
  contact = get_object_or_404(Contact, id=contact_id)
  return render(request, 'contacts/show_contact.html', {
    'contact': contact
  })
  