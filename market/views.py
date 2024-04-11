from django.core.paginator import Paginator, Page
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from market import models
from market.models import Books


# Create your views here.
# def get_products(request):
#     products = Books.objects.all()
#     item = []
#     for items in products:
#         item.append({
#             'name': items.name,
#             'page_count': items.page_count,
#             'category': items.category,
#             'author_name': items.author_name,
#             'price': items.price,
#             'image': items.image.url
#         })
#
#     return JsonResponse(item, safe=False)

def get_products(request):
    products = Books.objects.all()
    return JsonResponse(list(products.values()), safe=False)


def get_product(request, product_id):
    product = Books.objects.filter(id=product_id).first()
    return render(request, 'products/detail.html', {'product': product})
    # if product:
    #     product_data = models.Product.objects.get(id=product_id)
    # else:
    #     product_data = "Not found"
    # return JsonResponse(product_data)


# def get_product(request, product_id):
#     product = Books.objects.get(pk=product_id)
#     item = {
#         'name': product.name,
#         'page_count': product.page_count,
#         'category': product.category,
#         'author_name': product.author_name,
#         'price': product.price,
#         'image': product.image.url
#     }
#     return JsonResponse(item)


def index(request):
    queryset = Books.objects.all()
    paginator = Paginator(queryset, 3)
    page_number = int(request.GET.get('page', 1))
    # print(type(page_number))
    page: Page = paginator.get_page(page_number)
    # print(type(page))
    # print(page.object_list)
    # # return render(request, 'index.html')
    return render(request, 'index.html', {'page': page})
    # # return HttpResponse("Hello, world. You're at the polls index.")
