from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.shortcuts import render
from catalog import models as cmod
import math


@view_function
def process_request(request, product_id):
    selected_product = cmod.Product.objects.filter(id=product_id).first()
    if selected_product:
        page_title = selected_product.name
    else:
        page_title = 'Name of product goes here'

    context = {
        'page_title': page_title,
        'product': selected_product,
        'product_images': selected_product.image_urls(),
        jscontext('product_id'): product_id,
    }
    request.session['product_id'] = product_id
    return request.dmp.render('details.html', context)

