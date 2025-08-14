from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'myapp/home.html')


def about(request):
    return render(request, 'myapp/about.html')

def skills(request):
    return render(request, 'myapp/skills.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Send email to yourself
        send_mail(
            subject=f"New Contact from {name}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}",
            # message=f"Name: {name}\nEmail: {email}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['kharwaranshukumar@gmail.com'],  # my host email
        )

        return render(request, 'myapp/contact.html', {'success': True})

    return render(request, 'myapp/contact.html') 

# end of the sending email process