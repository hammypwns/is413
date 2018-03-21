from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from catalog import models as cmod
import math

@view_function
def process_request(request, prod_id=None):
    # Get product from url, default to None if no URL parameter
    try:
        product = cmod.Product.objects.filter(id=prod_id)[0]
        prod_name = product.name
        cat_name = product.category.name
    except Exception as e:
        return e

    context = {
        'product'   : product,
        'prod_name' : prod_name,
        jscontext('cat_name') : cat_name
    }

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

    return request.dmp.render('detail.html', context)
