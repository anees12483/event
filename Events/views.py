from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import EventModelForm
from .models import EventModel,EventBookings
from django.contrib.auth.decorators import login_required

def MadeEvent(request):
    form = EventModelForm()
    if request.method == "POST":
        form = EventModelForm(request.POST,request.FILES)
        if form.is_valid():
            data  = form.save()
            data.EventProvider = request.user
            data.save()
            messages.info(request,"Event Added To list")
            return redirect("MadeEvent")
    context = {
        "form":form
    }
    return render(request,"Admin/Add_event.html",context)

def AdminHome(request):
    return render(request,"Admin/adminhome.html")

def ViewEvents(request):
    events = EventModel.objects.filter(EventProvider = request.user)
    context = {
        "events":events
    }
    return render(request,"Admin/view_event.html",context)

@login_required(login_url="SignIn")
def EventBooking(request,pk):
    Event = EventModel.objects.filter(EventID=pk)
    event = EventModel.objects.get(EventID=pk)

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST['phone']
        numgust = request.POST['gnumber']
        eventTime = request.POST["time"]
        dateofevent = request.POST["date"]
        address  = request.POST["address"]
        
        events = EventBookings.objects.create(EventID = event,
                                              BookedBY =request.user, 
                                              EventDate = dateofevent, 
                                              Name = name,
                                              Address = address,
                                              Phonenumber  = phone,
                                              Email = email,
                                              EventTime = eventTime,
                                              GuestNumber = numgust
                                              )
        events.save()
        messages.info(request,"Event Booked Success")
        return redirect('EventBooking',pk = pk)
    context={
        "Event":Event
    }
    return render(request,"Eventbook.html",context)


@login_required(login_url="SignIn")
def Bookings(request):
    Booking = EventBookings.objects.filter(BookedBY = request.user)
    if request.method == "POST":
        id = request.POST["id"]
        date = request.POST["date"]
        Event = EventBookings.objects.get(BookingID=id)
        Event.EventDate = date
        Event.save()
        messages.info(request,"Date Changed")
        return redirect('Bookings')
    context = {
        "Booking":Booking
    }
    return render(request,'bookings.html',context)

@login_required(login_url="SignIn")
def BookingsAdmin(request):
    Event = EventModel.objects.filter(EventProvider = request.user)
    booking = EventBookings.objects.all()
    if request.method == "POST":
        id = request.POST["id"]
        Event = EventBookings.objects.get(BookingID=id)
        Event.delete()
        messages.info(request,"Booking Canceled")
        return redirect('BookingsAdmin')
    context = {
        "booking":booking
    }
    return render(request,"Admin/bookingsAdminview.html",context)

def DeleteEvent(request,pk):
    event = EventModel.objects.get(EventID = pk)
    event.delete()
    messages.info(request,"Event deleted success ")
    return redirect("ViewEvents")

def DeleteEventUser(request,pk):
    event = EventBookings.objects.get(BookingID = pk)
    event.delete()
    messages.info(request,"Booking deleted success ")
    return redirect("Bookings")
