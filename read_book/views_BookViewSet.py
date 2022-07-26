from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from read_book.models import Book
from read_book.permissions import IsOwnerOrStaffOrReadOnly
from read_book.serializers import BooksSerializer

# old view
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filter_fields = ['name', 'price', 'author_name'] # по каким полям хотим фильтровать
    search_fields = ['name', 'author_name'] # по каким полям хотим искать
    ordering_fields = ['name', 'price', 'author_name'] # сортировка

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()
