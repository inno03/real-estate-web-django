
from django.contrib import admin
from django.urls import path
from listings.views import listing_list, listing_retriev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list)
    path('listings/<pk>/', listing_retr)
]
