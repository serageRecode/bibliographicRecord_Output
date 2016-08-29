from django.conf.urls import url,include
from polls import views

urlpatterns=[
    url(r'^$', views.main_post, name='main_post'),
]
