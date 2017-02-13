from rest_framework import serializers
from wishlist_api.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book class
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('title', 'author',
                  'isbn', 'date_pub')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User class
    """

    books = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Book.objects.all()
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'email', 'password')
