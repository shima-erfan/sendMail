from django.shortcuts import render, redirect
from .models import MailAddress
from .forms import Mailform

# send email
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def mails(request):
    mails = MailAddress.objects.all()
    context = {'mails' : mails}
    return render(request, 'mails/mails.html', context)


def addMail(request):
    form = Mailform()
    
    if request.method == 'POST':
        form = Mailform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('mails')
        
    context = {'form' : form}
    return render(request, 'mails/add-mail-form.html', context)

def updateMail(request, pk):
    mail = MailAddress.objects.get(id=pk)
    form = Mailform(instance=mail)

    if request.method == 'POST':
        form = Mailform(request.POST, instance=mail)
        if form.is_valid:
            form.save()
            return redirect('mails')
        
    context = {'form' : form}
    return render(request, 'mails/add-mail-form.html', context)


def deleteMail(request, pk):
    mail = MailAddress.objects.get(id=pk)
    mail.delete()
    return redirect('mails')


def sendMails(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', None)
        massage = request.POST.get('massage', None)
        
        # fetch email addresses from database
        addresses = []
        obj = MailAddress.objects.all()
        for address in obj:
            addresses +=[address.address]
        
        # send emails
        send_mail(
            subject,
            massage,
            settings.EMAIL_HOST_USER,
            addresses,
            fail_silently= False,
        )


        return redirect('mails')
    return render(request, 'mails/mail-massage-form.html')
