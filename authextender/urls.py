from django.conf.urls import url
from django.contrib.auth import views

from authextender.forms import *
from authextender.views import ProfileView
from common.views import FormView, DetailView

urlpatterns = [
    url(r'^login/$', views.login, {'authentication_form': AuthenticationForm}, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^password_change/$', views.password_change, {'password_change_form': PasswordChangeForm}, name='password_change'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, {'password_reset_form': PasswordResetForm}, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, {'set_password_form': SetPasswordForm}, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
    url(r'^register/$', FormView.as_view(form_class=UserCreationForm), name='register'),
    url(r'^profile/(\d+)/$', ProfileView.as_view(), name='profile'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
]
