from django.http.response import HttpResponse
from django.shortcuts import render
from decouple import config
import smtplib
from twilio.rest import Client

# Create your views here.
def send_notification(request):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    Emailid = config('EmailId')
    password= config('Password')
    server.login(Emailid, password)
    msg = "hello :)"
    subject = " Demo Mail"
    body = "Subject: {}\n\n{}".format(subject,msg)
    server.sendmail(Emailid, 'amith.nc@apisero.com', body)
    

    #for message:
    account_sid = 'ACd8699836ee0052a11d61d2dfdf5643df'
    auth_token = config('AuthToken')
    client = Client(account_sid, auth_token) 
    message = client.messages.create(  
                              messaging_service_sid='MG3b3e70c06ee9facda0ff8abaf7175875', 
                              body='Hello',      
                              to='+919110673198' ) 
    print(message.sid)
    return HttpResponse("notification sent")