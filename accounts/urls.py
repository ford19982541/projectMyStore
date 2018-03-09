from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
urlpatterns =[
    url(r'^$',views.home ,name='home'),
    url(r'^login/$',views.login,name='login'),
    url(r'^contact/$',views.contact,name='contact'),
]