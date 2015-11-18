from django.http import Http404
from django.shortcuts import get_object_or_404

from authextender.models import User
from common.views import DetailView


class ProfileView(DetailView):
    model = User

    def get_object(self, queryset=None):
        if self.args:
            return get_object_or_404(User, pk=int(self.args[0]))
        if self.request.user.is_authenticated():
            return self.request.user
        raise Http404('You are not logged in, but you\'re looking for your own profile')