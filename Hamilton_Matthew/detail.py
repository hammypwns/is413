from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django_mako_plus import view_function, jscontext
from formlib import Formless
from django.utils import dateparse
from datetime import datetime, timezone
from catalog import models as cmod

@view_function
def process_request(request, product_id):

    if not request.user.is_authenticated:
        return HttpResponseRedirect("/account/login/")

    utc_time = datetime.utcnow()
    category_id = 0
    page_title = "Details"

    print(product_id)

    #selects proper product
    if cmod.Product.objects.filter(id = product_id).count() > 0:
        product = cmod.Product.objects.get(id = product_id)
        print(product.__class__.__name__)
        #gets all product images
        images = product.image_urls()
        print(images)
        category_id = product.category.id
        page_title = product.name


    #deals with category left hand pane


    context = {
        'utc_time': utc_time,
        "category_id" : category_id,
        "pagetitle" : page_title,
        "product" : product,
        'images' : images,
        jscontext("default_image") : product.image_url(),
        jscontext('js_category_id') : category_id,
    }

    request.session['new_prod'] = int(product_id)

    return request.dmp.render('detail.html', context)