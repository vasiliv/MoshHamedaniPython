from twilio.rest import Client

account_sid = "AC247a2911850d75b3b3bb8f78c105c8f3"
auth_token = "b2d8dc8624df1a4f2e131593939bb844"

client = Client(account_sid,auth_token)

# interesting attributes
# client.calls
# client.chat
call = client.messages.create(
    to="+995599930590",
    from_="+15155199793",
    body="Shota shens dedas shesca cminda giorgim"
)

