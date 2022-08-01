from django.shortcuts import render
from .models import Stock

# Create your views here.
def index(request):
    return render(request, "wap/index.html", { "stock": Stock.objects.all() })

def upload(request):
    pass
