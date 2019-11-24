from django.shortcuts import render

from french.models import French, Phrase, Verber, Verbre, Verbir


def home(request):
    return render(request, "home.html")
def index(request):
    debts = French.objects.all()
    return render(request, "index.html", {'debts': debts})

def phrase(request):
    debtp = Phrase.objects.all()
    return render(request, "phrase.html", {'debtp': debtp})

def erending(request):
    debter = Verber.objects.all()
    return render(request, "er.html", {'debter': debter})
def reending(request):
    debtre= Verbre.objects.all()
    return render(request, "re.html", {'debtre': debtre})
def irending(request):
    debtir= Verbir.objects.all()
    return render(request, "ir.html", {'debtir': debtir})