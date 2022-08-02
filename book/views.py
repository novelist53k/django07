from django.shortcuts import redirect, render
from .models import Book

# Create your views here.
def index(request):
    context = {
        "bset" : request.user.book_set.all(),
    }
    return render(request, "book/index.html", context)

def create(request):
    if request.method == "POST":
        Book(site_name=request.POST.get("sname"), maker=request.user,
             site_url=request.POST.get("surl"), site_con=request.POST.get("scon"), impo=bool(request.POST.get("impo"))).save()
        return redirect("book:index")

    return render(request, "book/create.html")
