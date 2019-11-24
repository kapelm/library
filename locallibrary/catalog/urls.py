from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
      path('', views.index, name='index'),
      url(r'^books/$', views.BookListView.as_view(), name='book_list'),
      url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
      url(r'^authors/$', views.AuthorListView.as_view(), name='author_list'),
      url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author_detail'),

]

вапрыварыр
