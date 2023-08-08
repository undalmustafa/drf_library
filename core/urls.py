from django.urls import path
from core.views import BookItemsGet, BookItemsPost, BookDetail

urlpatterns = [
    path('books/get/', BookItemsGet.as_view()),
    path('books/post/', BookItemsPost.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),
]