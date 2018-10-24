from django.conf.urls import url
from main.views import HomeView, get_data
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('snippets.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/get_data/', get_data, name='get_data'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
