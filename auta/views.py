from django.shortcuts import render, redirect
from .models import Auto, Zakaznik
from .forms import ZakaznikForm

def index(request):
    auta = Auto.objects.all()
    zakaznici = Zakaznik.objects.all()
    return render(request, 'index.html', {'auta': auta, 'zakaznici': zakaznici})

def auta(request):
    auta = Auto.objects.all()
    return render(request, 'auta.html', {'auta': auta})

def zakaznici(request):
    zakaznici = Zakaznik.objects.all()
    return render(request, 'zakaznici.html', {'zakaznici': zakaznici})

def register(request):
    if request.method == 'POST':
        form = ZakaznikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zakaznici')  # Po registraci přesměruj na seznam zákazníků
    else:
        form = ZakaznikForm()
    return render(request, 'register.html', {'form': form})
