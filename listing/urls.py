from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from listing.views import listing_list , listing_retrieve ,listing_create,listing_update,listing_delete
urlpatterns = [
    path("",listing_list,name=""),
    path("listing/<id>",listing_retrieve,name=""),
    path("create/",listing_create,name=""),
    path("listing/<id>/edit/",listing_update,name=""),
    path("listing/<id>/delete/",listing_delete,name=""),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)