from django.contrib.auth.forms import *
from django.core.urlresolvers import reverse

from common.crispymixin import CrispyMixin


class UserCreationForm(CrispyMixin, UserCreationForm):
    pass


class UserChangeForm(CrispyMixin, UserChangeForm):
    pass


class AuthenticationForm(CrispyMixin, AuthenticationForm):
    title = 'Login'
    name = 'login'
    post_text = '<p><a href="{% url "password_reset" %}">Lost password?</a></p>'


class PasswordResetForm(CrispyMixin, PasswordResetForm):
    title = 'Reset Password'
    name = 'password_reset'
    pre_text = 'Forgotten your password? Enter your email address below, and we\'ll email instructions for setting a new one.'

class SetPasswordForm(CrispyMixin, SetPasswordForm):
    title = 'Set Password'
    pre_text = 'Please enter your new password twice so we can verify you typed it in correctly.'


class PasswordChangeForm(CrispyMixin, PasswordChangeForm):
    title = 'Change My Password'
    name = 'password_change'
    pre_text = 'Please enter your old password, for security\'s sake, and then enter your new password twice so we can verify you typed it in correctly.'


class AdminPasswordChangeForm(CrispyMixin, AdminPasswordChangeForm):
    pass
