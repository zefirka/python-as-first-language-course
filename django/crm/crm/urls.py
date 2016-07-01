from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='Python!'),
    url(r'^customer/new/(\w+)/?$', views.new_customer),
    url(r'^customer/(\w+)/?$', views.customer),
    url(r'^customer/(\w+)/buy/([\w\d\-]+)/?$', views.buy),
    url(r'^products$', views.products),

    url(r'^admin/', include(admin.site.urls)),
]
