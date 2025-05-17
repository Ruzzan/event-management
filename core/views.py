from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Contact
from events.models import Event

def home_view(request):
    featured_events = Event.objects.filter(featured=True,approved=True)[:4]
    context = {'events':featured_events}
    return render(request,'core/home.html',context=context)

def contact_view(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(
            full_name=full_name,
            email=email,
            message=message
        )
        messages.success(request,"Message sent successfully.")
        return redirect('contact')
    return render(request,'core/contact.html')