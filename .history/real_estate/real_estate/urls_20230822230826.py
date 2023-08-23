
from django.contrib import admin
from django.urls import path
from listings.views import listing

urlpatterns = [
    path('admin/', admin.site.urls),
]
