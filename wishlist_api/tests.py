from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from .views import BookList, BookDetail, UserList, UserDetail
import factory
import datetime

from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


from wishlist_api.models import Book


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'bob{}'.format(n))
    email = factory.Sequence(lambda n: 'bob{}@bob.com'.format(n))
    password = 'top_secret'
    first_name = factory.Sequence(lambda n: 'Bob{}'.format(n))
    last_name = factory.Sequence(lambda n: 'Smith{}'.format(n))


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    owner = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'title{}'.format(n))
    author = factory.Sequence(lambda n: 'author{}'.format(n))
    isbn = factory.Sequence(lambda n: '12234-111{}'.format(n))
    date_pub = datetime.date.today()


class UserModelTest(TestCase):
    """
    Testing Creating users
    """
    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        self.today = datetime.date.today()

    def test_user(self):
        """tests the profile is created when a user is saved (Factoryboy)"""
        self.assertEqual(User.objects.count(), 1)
        self.user = UserFactory.create()
        self.assertEqual(User.objects.count(), 2)


class BookModelTest(TestCase):
    """
    Testing the Book Model
    """
    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        self.book = BookFactory(owner=self.user)
        self.today = datetime.date.today()

    def test_book(self):
        """tests the profile is created when a user is saved (Factoryboy)"""
        self.assertEqual(Book.objects.count(), 1)
        self.assertTrue(self.book.owner == self.user)
        self.assertTrue(self.book.title == 'title0')
        self.assertTrue(self.book.author == 'author0')
        self.assertTrue(self.book.isbn == '12234-1110')
        self.assertTrue(self.book.date_pub == self.today)
        self.user = BookFactory.create()
        self.assertEqual(Book.objects.count(), 2)


class ViewGetTest(TestCase):
    """
    Test that the endpoints return a 200 status code for
        /users/
        /users/1/
        /books/
        /books/1/
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        self.book = BookFactory(owner=self.user)

    def test_user_list(self):
        request = self.factory.get('/users/')
        request.user = self.user
        response = UserList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_user_list_anonymousUser(self):
        request = self.factory.get('/users/')
        request.user = AnonymousUser()
        response = UserList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_user_detail(self):
        request = self.factory.get('/users/1/')
        request.user = self.user
        response = UserDetail.as_view()(request, pk='1')
        self.assertEqual(response.status_code, 200)

    def test_book_list(self):
        request = self.factory.get('/books/')
        request.user = self.user
        response = BookList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_book_detail(self):
        request = self.factory.get('/books/1/')
        request.user = self.user
        response = BookDetail.as_view()(request, pk='1')
        self.assertEqual(response.status_code, 200)


class BookTests(APITestCase):
    """
    Test cases for the Wishlist API Book
    """
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        # self.user = UserFactory.create()
        self.user = User.objects.create_user('testuser',
                                             email='test@user.com',
                                             password='top_secret')
        self.user.save()

    def _require_login(self):
        self.client.login(username='testuser', password='top_secret')

    def test_add_to_wishlist_authenticated(self):
        """
        Testing adding a book to the wishlist
        """
        self.client.force_login(self.user)
        response = self.client.post('/book/', {'title': 'Moby Dick'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_to_wishlist_not_authenticated(self):
        """
        Testing adding a book to the wishlist
        """
        request = self.factory.post('/book/', {'title': 'Moby Dick'})
        request.user = self.user
        response = BookList.as_view()(request)
        self.assertEqual(response.status_code, 403)
