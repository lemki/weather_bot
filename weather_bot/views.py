from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from viberbot.api.viber_requests import (
    ViberMessageRequest,
    ViberConversationStartedRequest,
    ViberSubscribedRequest,
    ViberUnsubscribedRequest
)
from viberbot.api.messages import (
    TextMessage,
    PictureMessage
)

from .viber_configure import viber
from .models import ViberUser


class CallbackView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CallbackView, self).dispatch(*args, **kwargs)

    def post(self, request):
        viber_request = viber.parse_request(request.body)
        print(viber_request)
        if isinstance(viber_request, ViberMessageRequest):
            viber_user = ViberUser.objects.get_or_create(
                viber_id=viber_request.sender.id,
                defaults={
                    'name': viber_request.sender.name,
                    'avatar': viber_request.sender.avatar
                }
            )
            if isinstance(viber_request.message, TextMessage):
                viber.send_messages(viber_request.sender.id, viber_request.message)
            elif isinstance(viber_request.message, PictureMessage):
                viber.send_messages(
                    viber_request.sender.id,
                    TextMessage(text='Спасибо за картинку!')
                )
        elif isinstance(viber_request, ViberUnsubscribedRequest):
            ViberUser.objects.update_or_create(
                viber_id=viber_request.user_id,
                defaults={
                    'is_active': False
                }
            )
        elif isinstance(viber_request, ViberSubscribedRequest):
            ViberUser.objects.update_or_create(
                viber_id=viber_request.user.id,
                defaults={
                    'is_active': True,
                    'name': viber_request.user.name,
                    'avatar': viber_request.user.avatar
                }
            )
            viber.send_messages(
                viber_request.user.id,
                TextMessage(text='Спасибо за подписку!', tracking_data='пользователь подписался')
            )
        return HttpResponse(status=200)
