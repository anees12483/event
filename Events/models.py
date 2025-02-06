from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.utils import timezone,dateformat

class EventModel(models.Model):
    Select = (
        ("Food","Food"),
        ("Photography","Photography"),
        ("Decorations","Decorations"),
        ("Beauty","Beauty"),
        ("FullEvent","FullEvent"),
        
        )
    EventID = models.AutoField(primary_key=True)
    Event_Name = models.CharField(max_length=255)
    Event_Catogary = models.CharField(max_length=255,choices=Select)
    Event_Price = models.PositiveIntegerField()
    Event_Discription = models.CharField(max_length=1000)
    Time= models.CharField(max_length=100,null=True)
    Image = models.ImageField(upload_to="Eventimage")
    InstaID = models.CharField(max_length=255)
    Advance_Payment = models.PositiveIntegerField()
    EventProvider = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
class EventBookings(models.Model):
    BookingID = models.AutoField(primary_key=True,)
    EventID = models.ForeignKey(EventModel,on_delete=models.CASCADE)
    BookedBY = models.ForeignKey(User,on_delete=models.CASCADE)
    BookedDate = models.DateField(auto_now_add=True,auto_created=True)
    EventDate = models.DateField(auto_now_add=False)
    EventTime= models.CharField(max_length=100,null=True)
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=1000)
    Phonenumber = models.PositiveIntegerField() 
    Email = models.CharField(max_length=255)
    Approval_Status = models.BooleanField(default=True)
    GuestNumber = models.PositiveIntegerField()

   

