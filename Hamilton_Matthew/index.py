from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from catalog import models as cmod

@view_function
def process_request(request, category_id):

    if not request.user.is_authenticated:
        return HttpResponseRedirect("/account/login/")

    utc_time = datetime.utcnow()
    
    selected_category = cmod.Category.objects.filter(id=category_id)
    if selected_category.count() > 0:
        prod_count = int(cmod.Product.objects.filter(category = category_id).count())
        page_title = selected_category[0].name
        print(page_title)
        print("found selected category")
    else:
        prod_count = int(cmod.Product.objects.all().count())
        page_title = 'Products'
        print("didn't find category")


    num_pages = 0
    if prod_count % 6 > 0:
        num_pages += 1
    num_pages += (prod_count / 6)
    num_pages = int(num_pages)

    start_num = int(0)
    current_page = 1 

    print(page_title)
    context = {
        # sent to index.html:
        'utc_time': utc_time,
        # sent to index.html and index.js:
        jscontext('utc_epoch'): utc_time.timestamp(),
        
        'pagetitle': page_title,
        'category_id' : category_id,
        'numpages' : num_pages,
        'startnum' : start_num,
        jscontext('num_pages') : num_pages,
        jscontext('current_page') : current_page,
        jscontext('js_category_id') : category_id,
        }

    if not request.user.is_authenticated:
        return HttpResponseRedirect("/homepage/index/")
    return request.dmp.render('index.html', context)


@view_function
def products(request, category_id, current_page):

    start_num = int(0)
    end_num = int(6)

    print("category_id: " + category_id)  
    
    selected_category = cmod.Category.objects.filter(id=category_id)
    if selected_category.count() > 0:
        products = cmod.Product.objects.filter(category = category_id)
    
    else:
        products = cmod.Product.objects.all()
    
    if (current_page):
        start_num = int(current_page)
        start_num -= 1
        start_num *= 6
        print(start_num)
        end_num = int(start_num + 6)
        print(end_num)

    context = {
        'products': products,
        'start_num' : start_num,
        'end_num' : end_num,
        }

    request.session['new_prod'] = 0

    return request.dmp.render('index.products.html', context, {
        }
    )