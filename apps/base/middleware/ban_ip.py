from django.http import HttpResponseForbidden

class IPBanMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_ban_list = ['156.195.123.253','156.195.33.182']

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address in self.ip_ban_list:
            return HttpResponseForbidden('You are banned,Sorry :)')
        response = self.get_response(request)
        return response
                            

