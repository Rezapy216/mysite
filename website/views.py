from django.shortcuts import render
from django.contrib import messages
from website.forms import NameForm, ContactForm
from django.http import HttpResponse, JsonResponse
import json


def index_view(request):
    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submitted")
    form = ContactForm()
    return render(request, "website/contact.html", {'form': form})



def elements_view(request):
    return render(request, "website/elements.html")

