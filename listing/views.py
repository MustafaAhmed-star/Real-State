from django.shortcuts import render
from .models import Listing
# Create your views here.
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listing':listings}
    return render(request,'listing.html',context)    


def listing_retrieve(request , id):
    listing = Listing.objects.get(id=id)
    context = {
        'retrieve':listing}
    return render(request,'listing_D.html',context)        