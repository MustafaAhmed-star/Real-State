
from django.urls import path
from listing.views import listing_list , listing_retrieve
urlpatterns = [
    path("",listing_list,name=""),
    path("listing/<id>",listing_retrieve,name=""),
]
