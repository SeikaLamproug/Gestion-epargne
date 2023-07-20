from epargne import settings
from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'AC8d906c3dfb588b8daf500ccc9a7bdf96'
TWILIO_AUTH_TOKEN = '2f2088b159a4c78fd35c0cea40e59f59'
TWILIO_PHONE_NUMBER = '+13613226711'

def send_sms(to_phone_number, message):
    agent = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = agent.messages.create(
        body=message,
        from_= '+13613226711',
        to=to_phone_number
    )
    return message.sid