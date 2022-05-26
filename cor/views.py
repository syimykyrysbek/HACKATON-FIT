from django.http import HttpResponseRedirect
from django.shortcuts import render
from cor.models import  Contact1
# Create your views here.

def a(request):
    return render(request, 'index.html')


def sendContact(request):
    if request.method == 'POST':
        contact = Contact1()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.adress = request.POST.get('adress')
        contact.messages = request.POST.get('messages')
        contact.save()

        return HttpResponseRedirect('/')