from django.shortcuts import render
from .models import Listing
from .forms import Listingform

# Create your views here.

def listing_list(request):
  listings = Listing.objects.all()
  context = {
    "listings": listings
  }
  return render(request, "listings.html", context)

def listing_retrieve(request, pk):
  listing = Listing.objects.get(id=pk)
  context = {
    'listing': listing
  }
  return render(request, "listings.html", context)
