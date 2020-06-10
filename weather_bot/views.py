from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .viber_configure import viber


class CallbackView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CallbackView, self).dispatch(*args, **kwargs)

    def post(self, request):
        viber_request = viber.parse_request(request.body)
        print(viber_request)
        return HttpResponse(status=200)
