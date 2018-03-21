from catalog import models as cmod

class LastFiveMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # one-time configuration and initialization

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # request.session['last_five'] = [91,92,93,94,95,96,97,98] #Initialize if needed
        # Initialize new_prod_id
        # request.session['last_five'] = [33]
        # request.session['new_prod'] = 1
        if request.session.get('new_prod') == None:
            print("the truth has came!!!^!!!^!^!^!^!")
            request.session['new_prod'] = 0
        if request.session.get('last_five') == None:
            print(" ANTOEHR Truth iS NEIGH")
            request.session['last_five'] = []
        new_prod_id = int(request.session['new_prod'])

        if new_prod_id != 0:
            # Not on an index page
            if new_prod_id in request.session['last_five']:
                # remove, item is already in the list
                request.session['last_five'].remove(new_prod_id)
            else:
                # Add Product to first of the last 5 shown
                request.session['last_five'].insert(0, int(new_prod_id))

        # Create list to display in right block in app_base.htm
        request.last_five = []
        for i in request.session['last_five']:
            request.last_five.append(cmod.Product.objects.get(id = i))

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        # Reset 'last_five' dictionary with the five items currently displayed
        request.session['last_five'] = []
        for product in request.last_five:
            request.session['last_five'].append(product.id)
        # Keep the array small
        while len(request.session['last_five']) > 5:
            request.session['last_five'].pop()

        return response