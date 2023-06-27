class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        request_data = {
            'method': request.method,
            'path': request.path,
            'headers': dict(request.headers),
            'params':request.params
        }