from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

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
  if term == None:
    messages.add_message(request, messages.ERROR, 'give me a search...')
    return redirect('contacts.index')
  fields = Concat('name', Value(' '), 'last_name')
  contacts = Contact.objects.annotate(name_full=fields).filter(
    Q(phone__icontains=term) | Q(name_full__icontains=term),
  )
  paginator = Paginator(contacts, 3)
  contacts_paginator = paginator.get_page(term)
  if len(contacts) == 0:
    messages.add_message(request, messages.INFO, f'Found 0 result, ...')
    messages.add_message(request, messages.INFO, f'do it again with other key...')
  else:
    messages.add_message(request, messages.SUCCESS, f'Found {len(contacts)} results')
  return render(request, 'contacts/search.html', {
    'contacts': contacts_paginator
  })
