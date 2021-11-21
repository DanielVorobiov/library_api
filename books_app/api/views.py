from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        page_nr = self.request.query_params.get('page_nr')
        if page_nr is not None:
            queryset = queryset.filter(page_nr = page_nr)
        return queryset
    


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
