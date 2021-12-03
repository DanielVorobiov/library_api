from django.shortcuts import render
from djproxy.views import HttpProxy

class ReverseProxy(HttpProxy):
    base_url = 'http://127.0.0.1:8000/api/'
    