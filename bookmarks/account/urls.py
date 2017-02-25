from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    # post views
    url(r'^login/$', views.user_login, name='login'),

    # login/ logout urls
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
]