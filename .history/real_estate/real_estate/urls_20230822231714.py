
from django.contrib import admin
from django.urls import path
from listings.views import listing_list, listing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list)
]
