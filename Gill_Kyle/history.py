from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(get_response)
        
    
    def __call__(self, request):
        print("_________________ START BEFORE REQUEST _________________")
        # assigns product id from the details.py to the url param or 0
        product_id = int(request.session['product_id'])
        # if there is a product id, perform, otherwise do nothing
        if product_id != 0:
            if product_id in request.session['recently_viewed']:
                print("Removing duplicate product id: ")
                print(product_id)
                request.session['recently_viewed'].remove(product_id)
            
            print("Adding product id: ")
            print(product_id)
            request.session['recently_viewed'].insert(0, product_id)

        request.recently_viewed = []

        print(request.session['recently_viewed'])
        for i in request.session['recently_viewed']:
            print("Adding product to recently_viewed array with id: " + str(i))
            request.recently_viewed.append(cmod.Product.objects.get(id = i))
        
        print("_________________ END BEFORE REQUEST _________________")
        response = self.get_response(request)
        print("_________________ START AFTER REQUEST _________________")

        request.session['recently_viewed'] = []

        for product in request.recently_viewed:
            request.session['recently_viewed'].append(product.id)
            print(product.name)

        while len(request.session['recently_viewed']) > 6:
            request.session['recently_viewed'].pop()

        print("_________________ END AFTER REQUEST _________________")
        return response



    
