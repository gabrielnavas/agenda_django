from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from .models import Contact

def index(request):
  contacts = Contact.objects.order_by('-id').filter(is_show=True)
  paginator = Paginator(contacts, 3)
  page=request.GET.get('p')
  contacts_paginator = paginator.get_page(page)
  return render(request, 'contacts/index.html', {
    'contacts': contacts_paginator
  })


def show_contact(request, contact_id):
  contact = get_object_or_404(Contact, id=contact_id)
  if not contact.is_show:
    raise Http404()
  return render(request, 'contacts/show_contact.html', {
    'contact': contact
  })
  