from django.urls import path
from core.views import BookItems, BookDetail

urlpatterns = [
    path('books/', BookItems.as_view({"get": "list"})),
    path('books/post/', BookItems.as_view({"post": "create"})),
    path('books/<slug:slug>/', BookDetail.as_view({"get": "list"})),
    path('books/<uuid:id>', BookDetail.as_view({"get": "list_id"})),
    path('books/delete/<uuid:id>', BookDetail.as_view({"delete": "destroy"})),
    path('books/update/<uuid:id>', BookDetail.as_view({"put": "update"}))

]