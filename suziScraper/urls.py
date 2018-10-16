from django.conf import settings
from django.conf.urls import url, static
from django.views.generic import TemplateView
from main.views import HomeView, get_data
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/get_data/', get_data, name='get_data'),
    path('admin/', admin.site.urls),
]
