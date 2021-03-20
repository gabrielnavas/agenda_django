from django.shortcuts import render

def index(request):
  render(request, 'contacts/index.html')