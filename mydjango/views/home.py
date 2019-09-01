from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView
from people.models import User


class Index(View):
    def get(self, request):
        return HttpResponse("hello world")


class UserList(ListView):
    model = User  # 要显示详情内容的类

    template_name = 'user/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        users = User.objects.all()
        print('users：', users)
        return users


def home(request):
    return HttpResponse('hi home')
