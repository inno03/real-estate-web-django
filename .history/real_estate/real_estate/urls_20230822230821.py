
from django.contrib import admin
from django.urls import path
from listings.views import

urlpatterns = [
    path('admin/', admin.site.urls),
]
