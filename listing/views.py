from django.shortcuts import redirect, render
from .models import Listing
from .forms import ListingForm
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


def listing_create(request):
    form = ListingForm()
    if request.method== "POST":
        form = ListingForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            print("hey")
            form = ListingForm()

    context = {
        "form":form
    }
    return render(request,'listing_form.html',context)
def listing_update(request,id):
    listing = Listing.objects.get(id=id)
    form =ListingForm(instance=listing)
    if request.method== "POST":
        form = ListingForm(request.POST, instance=listing,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = ListingForm()

    context = {
        "form":form
    }
    return render(request,'listing_update.html',context)
def listing_delete(request,id):
    listing = Listing.objects.get(id=id)
    listing.delete()
 
    return redirect("/")
