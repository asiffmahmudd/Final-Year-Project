from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from .models import  Product
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages
from .filters import ProductFilter
import random
from machina import MACHINA_MAIN_TEMPLATE_DIR

from django.views.generic import ListView, DetailView



def index(request):
    post = Product.objects.all().order_by("?")

    context = {
        "post":post
    }
    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact-us.html")

#
# def forum(request):
#     return HttpResponseRedirect(MACHINA_MAIN_TEMPLATE_DIR)


def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:  # if accepted
                login(request, auth)
                return redirect('index')
    return render(request, "login.html")


def getLogout(request):
    logout(request)
    return redirect('index')


def searchProduct(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Product.objects.filter(Q(product_name__icontains=srch)
                                                 | Q(vendor_name__icontains=srch))
            if match:
                return render(request, 'search.html', {'sr':match})
            else:
                messages.error(request, 'No result found')

        else:
            return HttpResponseRedirect('search')
    return render(request, 'search.html')

def tablesorter(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Product.objects.filter(Q(product_name__icontains=srch)
                                                 | Q(vendor_name__icontains=srch))
            if match:
                return render(request, 'tablesorter.html', {'sr':match})
            else:
                messages.error(request, 'No result found')

        else:
            return HttpResponseRedirect('tablesorter')
    return render(request, 'tablesorter.html')



def searchTable(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'searchTable.html', {'filter': product_filter})



