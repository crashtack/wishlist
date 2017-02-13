from rest_framework import generics
from django.contrib.auth.models import User
from wishlist_api.models import Book
from wishlist_api.serializers import BookSerializer, UserSerializer


class BookList(generics.ListCreateAPIView):
    """
    List all the books on the wishlist,
    or add a new one.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        """
        Associates a user with a wishlist entry
        """
        serializer.save(owner=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get details, update, or delete a wish list entry
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserList(generics.ListAPIView):
    """
    Get a list of users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Get a single users details
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
