from django.forms import ModelForm
from .models import EventModel

class EventModelForm(ModelForm):
    class Meta:
        model = EventModel
        fields = ["Event_Name","Event_Catogary","Event_Price","Event_Discription","Advance_Payment","InstaID","Image"]