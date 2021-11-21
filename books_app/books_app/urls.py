
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from proxy.views import ReverseProxy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    url(r'proxy/(?P<url>.*)$', ReverseProxy.as_view(), name='proxy')
]

