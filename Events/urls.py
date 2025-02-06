from django.urls import path
from .import views

urlpatterns = [
    path("MadeEvent",views.MadeEvent,name="MadeEvent"),
    path("AdminHome",views.AdminHome,name="AdminHome"),
    path("ViewEvents",views.ViewEvents,name="ViewEvents"),
    path("EventBooking/<int:pk>",views.EventBooking,name="EventBooking"),
    path("Bookings",views.Bookings,name="Bookings"),
    path("BookingsAdmin",views.BookingsAdmin,name="BookingsAdmin"),
    path("DeleteEvent/<int:pk>",views.DeleteEvent,name="DeleteEvent"),
    path("DeleteEventUser/<int:pk>",views.DeleteEventUser,name="DeleteEventUser"),
]
