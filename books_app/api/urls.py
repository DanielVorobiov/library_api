from django.urls import path
from api import views
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from books_app import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
urlpatterns = [
    path('', views.BookList.as_view()),
    path('<int:pk>/',  cache_page(CACHE_TTL)(views.BookDetail.as_view())),
]
