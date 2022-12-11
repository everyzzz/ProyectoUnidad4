from ipware import get_client_ip
from application.models import ip
from django.http import HttpResponse


BLACK_LIST = ['']

class IpIsValid():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip2, is_routable = get_client_ip(request)
        ip(ip=ip2).save()
        if ip in BLACK_LIST:
            return HttpResponse('Bad request', status=404)
        else:
            return self.get_response(request)





