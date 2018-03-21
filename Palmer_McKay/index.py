from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from catalog import models as cmod
import math

@view_function
def process_request(request, cat_id, pagenum:int=1):
    # cat_id used to get Category, pagenum set to 1 by default if not given
    try:
        query = cmod.Product.objects.all() # Gets all the products, modified if a category is selected

        if cat_id is not None: # If category isn't none, modify the query
            query = query.filter(category=cat_id)
            category = query[0].category # Gets the category object
            page_title = category.name # Gets the name of the category object
        else: # There is nothing after catalog/index/
            page_title = 'All Products'
    except Exception:
        return HttpResponseRedirect('/catalog/index') # Go here if url params are bad

    # Calculate number of products and pages needed if displaying 6 per page
    prod_count = int(query.count())
    numpages = math.ceil(prod_count / 6)

    # If pagenum not in range of 1 <--> numpages return to All Products
    if pagenum < 1 or pagenum > numpages:
        return HttpResponseRedirect('/catalog/index')

    # pagenum and cat_id passed to index.js context variable
    context = {
        'categories': cmod.Category.objects.all(),
        'page_title': page_title,
        'numpages' : numpages,
        jscontext('pagenum'): pagenum,
        jscontext('cat_id') : cat_id,
    }
    # don't do all the stuff if not on a product detail page.
    request.session['new_prod'] = 0
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect("/homepage/index/")
    return request.dmp.render('index.html', context)


@view_function
def products(request, cat:cmod.Category=None, pnum:int=1):
    #Set cat equal to none if nothing is there in the URL
    #Set pnum to 1 as defualt if nothing is there in the URL
    query = cmod.Product.objects.all()
    if cat is not None:
        #If category isn't none, modify the query
        query = query.filter(category=cat)

    products = query # different varibale name passed to context{}

    # Get range of products to query
    start_num = int((pnum * 6) - 6)
    end_num = int(pnum * 6)

    context = {
        'products': products,
        'start_num' : start_num,
        'end_num' : end_num,
        }

    return request.dmp.render('index.products.html', context, {
        }
    )
