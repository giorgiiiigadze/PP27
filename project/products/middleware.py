import time

class ProductMiddleware:
    # current time - last time 
    # last time - current time - time.time()
    def __init__(self, get_response):  # sawhiroa yvela custom middlewareshi 
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time() 
        response = self.get_response(request)
        duration = time.time() - start_time

        if request.path.startswith('/products/'):
            print(f'[Product] request to {request.path} took {duration:.3f} seconds')
        return response
        
