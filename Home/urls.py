from django.urls import path
from .import views

urlpatterns = [
    path("",views.EventHome,name="EventHome"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("EventGroupSignUp",views.EventGroupSignUp,name="EventGroupSignUp"),
    path("SignOut",views.SignOut,name="SignOut"),
]
