from django.shortcuts import render
from django.http import Http404
from .models import Contact

def index(request):
  contacts = Contact.objects.all()
  return render(request, 'contacts/index.html', {
    'contacts': contacts
  })


def show_contact(request, contact_id):
  try:
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contacts/show_contact.html', {
      'contact': contact
    })
  except Contact.DoesNotExist as e:
    raise Http404()