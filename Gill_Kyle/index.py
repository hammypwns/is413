from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.shortcuts import render
from catalog import models as cmod
import math


@view_function
def process_request(request, category_id, current_page: int = 1):
    selected_category = cmod.Category.objects.filter(id=category_id)
    if selected_category.count() > 0:
        page_title = selected_category[0].name
        print(page_title)
        print("found selected category")
        products = cmod.Product.objects.filter(category=category_id)
        number_of_pages = math.ceil(products.count() / 6)
    else:
        page_title = 'Products'
        print("didn't find category")
        products = cmod.Product.objects.all()
        number_of_pages = math.ceil(products.count() / 6)

    print(page_title)
    context = {
        'page_title': page_title,
        'products': products[:6],
        'number_of_pages': number_of_pages,
        jscontext('category_id'): category_id,
        jscontext('num_pages'): number_of_pages,
        jscontext('current_page'): current_page,
    }
    print(context)
    return request.dmp.render('index.html', context)


@view_function
def products(request, category_id: cmod.Category = None, page_num: int = 1):
    query = cmod.Product.objects.all()
    start = 6 * (page_num - 1)
    end = 6 * page_num
    print(category_id)
    if category_id is not None:
        query = query.filter(category=category_id)
    print(query)
    context = {'products': query[start:end]}
    return request.dmp.render('index.products.html', context)
