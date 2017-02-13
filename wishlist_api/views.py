from rest_framework import generics, permissions
from django.contrib.auth.models import User
from wishlist_api.models import Book
from wishlist_api.serializers import BookSerializer, UserSerializer
from wishlist_api.permissions import IsOwnerOrReadOnly


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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
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
