from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def info_item(request, id):
    pass

def buy_item(request, id):
    pass