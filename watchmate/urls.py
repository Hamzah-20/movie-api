from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Watchlist API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist_app.urls')),
    path('', home),
]