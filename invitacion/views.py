from django.shortcuts import render, redirect
from invitacion import models, forms

# Create your views here.

def homepage(request):
    if request.method == "POST":
        form = forms.Invitacion(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = forms.Invitacion()
    return render(request, "homepage.html", {"form":form})

def table_guests(request):
    query = models.Invitacion.objects.all()
    return render(request, "table_guests.html", {"query":query})

    