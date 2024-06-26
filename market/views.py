from django.core.paginator import Paginator, Page
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from market import models
from market.models import Books


def get_products(request):
    products = Books.objects.all()
    return JsonResponse(list(products.values()), safe=False)


def get_product(request, product_id):
    # product = Books.objects.filter(id=product_id).first()
    product = get_object_or_404(Books, id=product_id)
    return render(request, 'products/detail.html', {'product': product})


def index(request):
    queryset = Books.objects.all()
    paginator = Paginator(queryset, 3)
    page_number = int(request.GET.get('page', 1))
    page: Page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page})
