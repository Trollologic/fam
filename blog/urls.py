from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_view, name='main_view'),
    url(r'^test/', views.PostExample.as_view(), name='test-start'),
]