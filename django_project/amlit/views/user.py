__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '22/01/21'

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from amlit.serializer.user import UserSerializer

User = get_user_model()


class UserDetailView(View):
    template_name = 'page/detail.html'

    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        context = UserSerializer(user).data
        context['role'] = context['title']
        context['title'] = context['username']
        context['content_page'] = 'user/detail.html'
        return render(
            request, self.template_name, context=context
        )
