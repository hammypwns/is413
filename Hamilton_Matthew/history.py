from catalog import models as cmod

class LastFiveMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        #request.session stuff
        # Code to be executed for each request before
        # the view (and later middleware) are called.        
                    
        if not request.user.is_authenticated:
            request.session['new_prod'] = -1

        new_prod_id = int(request.session['new_prod'])
        print ("new_prod_id: ")
        print(new_prod_id)
        
        if new_prod_id > 0:
            print("woah")

            if new_prod_id in request.session['last_five']:
                print("the item is already in the list, removing: ")
                print(new_prod_id)
                request.session['last_five'].remove(new_prod_id)
            
            print("adding: ")
            print(new_prod_id)
            request.session['last_five'].insert(1, new_prod_id)

        request.last_five = []

        print(request.session['last_five'])


        for i in request.session['last_five']:
            print("i: " + str(i))
            request.last_five.append(cmod.Product.objects.get(id = i))

        

        response = self.get_response(request)

        request.session['last_five'] = []

        for product in request.last_five:
            request.session['last_five'].append(product.id)

        while len(request.session['last_five']) > 7:
            request.session['last_five'].pop()

        return response




# before the request:
    # product_ids = session.get ids from the sessions
    # ^ request.session sub whatever (which is a dictionary)
    # products = [ convert list of ids to actual objects]
    # request.last_five = [ store most recent 5 product objects (not ids)]
    # if product_id already exists in the list, remove it and add it back to the front

# in catalog/templates/app_base.htm:
    # do a for loop through the last 5
    # request.last_five

# in catalog/views/detail.py:
    # put current product being viewed into request.last_five

# view.py files DO NOT DO ANYTHING

# After request, in this file
    # convert request.last_five back to list of ids
    # set the list of ids into the session

#  ['flowers', 'ball', 'car', 'doll', 'dollie', 'beef]
    # actually keep 6
    # only display array[1:6]



    # request.last_five = []

    #     for i in request.session['last_five'][0:6]:
    #         print("i: " + str(i))
    #         request.last_five.append(cmod.Product.objects.get(id = i))

    #     print("request.last_five: ")
    #     print(request.last_five)
        
        
    #     response = self.get_response(request)



    #     new_prod_id = int(request.session['new_prod'])

    #     print("new prod: ")
    #     print(new_prod_id)

    #     print("before: ")
    #     print(request.session['last_five'])

    #     if new_prod_id not in request.session['last_five'][1:6]:
    #         print("we're good fam: ")
    #         print(new_prod_id)
    #         request.session['last_five'].insert(0, new_prod_id)

    #     else:
    #         print('already in')

    #     if new_prod_id in request.session['last_five'][0:6]:
    #         print("Is in last_five")
    #         request.session['last_five'].remove(new_prod_id)
    #         print("in the middle: ")
    #         print(request.session['last_five'])
    #         request.session['last_five'].insert(0, new_prod_id)

    #     else:
    #         print("Not in last_five")
    #         request.session['last_five'].insert(1, new_prod_id)
    #         while len(request.session['last_five']) > 6:
    #             print("pop: " + str(request.session['last_five'].pop()))

    #     while len(request.session['last_five']) > 6:
    #         print("pop: " + str(request.session['last_five'].pop()))

    #     print("after: ")
    #     print(request.session['last_five'])


    #   new_prod_id = int(request.session['new_prod'])
    #     print ("new_prod_id: ")
    #     print(new_prod_id)
        
    #     if new_prod_id > 0:
    #         print("woah")

    #     if new_prod_id in request.session['last_five']:
    #         print("the item is already in the list, removing: ")
    #         print(new_prod_id)
    #         request.session['last_five'].remove(new_prod_id)
            
    #         print("adding: ")
    #         print(new_prod_id)
    #         request.session['last_five'].insert(1, new_prod_id)

    #         request.last_five = []

    #         print(request.session['last_five'])

    #         for i in request.session['last_five']:
    #             print("i: " + str(i))
    #             request.last_five.append(cmod.Product.objects.get(id = i))

    #     response = self.get_response(request)

    #     if request.session['new_prod'] > 0:

    #         request.session['last_five'] = []

    #         for product in request.last_five:
    #             request.session['last_five'].append(product.id)

    #         while len(request.session['last_five']) > 7:
    #             request.session['last_five'].pop()

    #     request.session['new_prod'] = -1

    #     return response