""" Opinify URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import Homepage
from accounts import Signup, Login, Logout


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', Homepage.as_view(), name="homepage"),
    url(r'^polls/', include('poll.urls', namespace="poll")),
    url(r'^login$', Login.as_view(), name="login"),
    url(r'^signup$', Signup.as_view(), name="signup"),
    url(r'^logout$', Logout.as_view(), name="logout"),
    # url(r'^/', include()),
]
