from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Count

from .models import Event, Application

@login_required(login_url='login')
def create_event(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        price = request.POST.get('price',0)
        cover = request.FILES.get('cover')
        organizer = request.POST['organizer']
        phone_number = request.POST['phone_number']
        description = request.POST['description']
        print(name,date,time,location,price,cover,organizer,phone_number,description)
        event = Event.objects.create(name=name,date=date,time=time,location=location,phone_number=phone_number,price=price,organizer=organizer,cover=cover,description=description,user=user)
        return redirect(event.get_absolute_url)
    return render(request,'events/create.html')

def event_list(request):
    events = Event.objects.all().filter(approved=True)

    if request.method == 'GET':
        search_query = request.GET.get('search',None)
        if search_query:
            events = events.filter(name__icontains=search_query)

    # Number of items to display per page
    items_per_page = 12
    
    paginator = Paginator(events, items_per_page)
    
    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')
    
    try:
        # Get the page with the requested number
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), show the last page of results
        items = paginator.page(paginator.num_pages)
    
    return render(request, 'events/list.html', {'events': items,})

def event_detail(request,pk):
    event = get_object_or_404(Event.objects.all(),pk=pk)
    other_events = Event.objects.all().filter(approved=True).exclude(pk=event.pk)[:4]
    return render(request,'events/detail.html',{'event':event,'other_events':other_events})

def edit_event(request,pk):
    event = get_object_or_404(Event.objects.all(),pk=pk)
    user = request.user

    if user != event.user:
        return redirect("events-list")
    
    applications = event.applications.all()
    total = applications.count()

    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        price = request.POST.get('price',0)
        cover = request.FILES.get('cover',None)
        organizer = request.POST['organizer']
        phone_number = request.POST['phone_number']
        description = request.POST['description']

        event.name = name
        event.date = date
        event.time = time
        event.location = location
        event.price = price
        event.organizer = organizer
        event.phone_number = phone_number
        event.description = description
        if cover:
            event.cover = cover
        event.save()
        messages.success(request,"Event updated successfully.")
        return redirect(event.get_absolute_url)
    
    context = {
        "event":event,
        "applications":applications,
        "total":total
    }
    return render(request,'events/edit.html',context=context)
    

def delete_event(request,pk):
    event = get_object_or_404(Event.objects.all(),pk=pk)
    if request.user == event.user:
        event.delete()
        messages.success(request,"Event deleted successfully.")
        return redirect('my-events')
    return render(request,'events/create.html')

@login_required(login_url='login')
def register_event(request,pk):
    event = get_object_or_404(Event.objects.all(),pk=pk)
    if request.method == "POST":
        full_name = request.POST.get('full_name',None)
        email = request.POST.get('email',None)
        phone_number = request.POST.get('phone_number',None)
        address = request.POST.get('address',None)

        try:
            Application.objects.create(
                event=event,
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                address=address,
                user=request.user
            )
            messages.success(request,"Successfully registered to event.")
            return redirect(event.get_absolute_url)
        except Exception as e:
            print(e)
            messages.error(request,"An error occoured.")
            return redirect(event.get_absolute_url)
    return render(request,'events/detail.html',{'event':event,})


@login_required(login_url='login')
def my_events(request):
    user = request.user
    events = Event.objects.filter(user=user)
    context = {
        "events":events
    }
    return render(request,'events/my_events.html',context=context)

@login_required(login_url='login')
def my_registrations(request):
    user = request.user
    applications = Application.objects.filter(user=user)
    total = applications.count()
    context = {
        "applications":applications,
        "total":total,
    }
    return render(request,'events/my_registrations.html',context=context)