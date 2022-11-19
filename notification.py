from twilio.rest import Client
from number import phone_number, twilio_number
import os

TWILIO_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

class Notification:
    def __init__(self):
        pass
    
    def send_sms(self, message):
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        client.messages.create(
                            body=message,
                            from_=twilio_number,
                            to=phone_number
                        )
