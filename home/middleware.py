from django.http import HttpResponseRedirect

class RedirectToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            # Redirect to the home page
            return HttpResponseRedirect('/')
        return self.get_response(request)