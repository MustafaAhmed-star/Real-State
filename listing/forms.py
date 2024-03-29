from django.forms import ModelForm

from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields =[
    "title",  
    "price",
    "num_beds",
    "num_bathes",
    "square_footage",
    "address",
    "image",
           ]