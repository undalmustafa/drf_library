from django.urls import path
from core.views import BookItemsGet, BookItemsPost, BookDetail

urlpatterns = [
    path('books/', BookItemsGet.as_view()),
    path('books/post/', BookItemsPost.as_view()),
    path('books/<slug:slug>/', BookDetail.as_view()),
]