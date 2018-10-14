from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done

from . import views

#app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/password/$', views.change_password, name='change_password'),


    url(r'^password/reset/$', password_reset, {'template_name': 'accounts/reset_password.html',
                                               'post_reset_redirect': 'accounts:password_reset_done'}, name='password_reset'),


    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
]