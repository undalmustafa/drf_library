from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from core.models import Book
from core.serializers import BookSerializer
from rest_framework.viewsets import ViewSet

class BookItems(ViewSet):
    def list(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(ViewSet):
    def list(self, request, slug, format=None):
        try:
            book = Book.objects.filter(slug=slug)
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data)
        except Book.DoesNotExist:
            raise Http404

    def list_id(self, request, id, format=None):
        try:
            book = Book.objects.filter(id=id)
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data)
        except Book.DoesNotExist:
            raise Http404

    def destroy(self, request, id, format=None):
        try:
            book = Book.objects.filter(id=id)
            self.perform_destroy(book)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()