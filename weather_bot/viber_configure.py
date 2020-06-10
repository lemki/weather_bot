from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from django.conf import settings


bot_configuration = BotConfiguration(
    name='PipBot',
    avatar='https://www.prostir.ua/wp-content/uploads/2019/07/chatbot.png',
    auth_token=settings.VIBER_TOKEN
)
viber = Api(bot_configuration)


def set_webhook():
    webhook_events = [
        "failed",
        "subscribed",
        "unsubscribed",
        "conversation_started"
    ]
    viber.set_webhook('https://f6fc51a26d63.ngrok.io/bot/callback/', webhook_events=webhook_events)

