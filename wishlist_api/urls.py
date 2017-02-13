from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from wishlist_api import views


urlpatterns = [
    url(r'^book/$', views.BookList.as_view()),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
