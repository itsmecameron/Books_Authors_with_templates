from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add_book),
    url(r'^books/(?P<val>\d+)$', views.show_book),
    url(r'^add_author$', views.add_author),
    url(r'^authors$', views.author),
    url(r'^add_author$', views.add_author),
    url(r'^authors/(?P<val>\d+)$', views.show_author),
    url(r'^add_book$', views.add_book),
]


# url(r'^books$/(?P<val>\d+)', views.add_book)