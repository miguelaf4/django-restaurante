from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name','')
            email= request.POST.get('email','')
            content= request.POST.get('content','')

            #Enviar email
            subject = 'Gracias por contactarnos'
            message = f'Hola {name}, gracias por contactarnos, en un momento nos contactaremos contigo..' 
            message += "\n\n\n----------------------------\n\n\n" + content
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)

            return redirect(reverse('contact')+'?ok')
    return render(request, "contact/contact.html", {'form': contact_form})
