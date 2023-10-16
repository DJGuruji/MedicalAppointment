from django.http import HttpResponseRedirect

class RedirectToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
 
        if request.path.startswith('/admin/') and not request.user.is_staff and not request.user.is_superuser: # Redirect to the home page
            return HttpResponseRedirect('/')
        elif request.path.startswith('/appointment') and not request.user.is_staff and not request.user.is_superuser: # Redirect to the home page
            return HttpResponseRedirect('/')
        return self.get_response(request)
        