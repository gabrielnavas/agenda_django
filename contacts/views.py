from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

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
  

def search(request):
  term=request.GET.get('term')
  fields = Concat('name', Value(' '), 'last_name')
  contacts = Contact.objects.annotate(name_full=fields).filter(
    name_full__icontains=term
  )
  print(contacts.query)
  print(term)
  paginator = Paginator(contacts, 3)
  contacts_paginator = paginator.get_page(term)
  return render(request, 'contacts/search.html', {
    'contacts': contacts_paginator
  })
