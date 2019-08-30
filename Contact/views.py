from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
# Create your views here.
 
def msg(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        email=request.POST['email']
        country=request.POST['country']
        subject1=request.POST['subject']
        c1=Contact(name=fname,email=email,country=country,msg=subject1)
        c1.save()
        subject = 'Thank you for for Contacting us.'
        message = 'Thank you for for Contacting us. We will get back to you soon. '
        info= str(fname) + "  \n"  + str(email) + "  \n" + str(country) +" \n" +str(subject1)
        message= message + " \n " + info
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['aneelomani@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/')

    else:
        return render(request,'Contact.html')