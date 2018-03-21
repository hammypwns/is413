from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django import forms
import re
from catalog import models as cmod
import math
from django.conf import settings
from datetime import datetime, timezone
from django.shortcuts import render


@view_function
def process_request(request, prod_id=None):
    product = cmod.Product.objects.filter(id=prod_id)[0]
    cName = product.category

    underline = int(cmod.Category.objects.filter(name=cName)[0].id)

    myCategories = cmod.Category.objects.all()

    images = product.image_urls()
    path = product.image_url()
    myList = []
    for im in images:
        myList.append(str(im.filename))

#put current product being viewed into the request.lastFive
    print("My PIDPIDPID " + str(product.id))
    # Assign ID of currently viewed product to request.session['new_prod']
    request.session['new_prod'] = product.id

    # Check see if product is in request.session['last_five'] dict value
    if int(prod_id) in request.session['last_five']:
        # Requested to view Product that will show in right_list, need to remove
        request.session['last_five'].remove(int(prod_id))
        # Create request.last_five array to be rendered by right block in app_base.htm
        request.last_five = []
        for i in request.session['last_five']:
            request.last_five.append(cmod.Product.objects.get(id = i))

    return request.dmp.render('detail.html', {
        'categories': myCategories,
        jscontext('imagePath'): path,
        'images': images,
        'product': product,
        'underline': underline,
    })