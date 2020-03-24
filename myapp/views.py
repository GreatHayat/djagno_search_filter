from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter
# Create your views here.


def index(request):
    users = User.objects.all()
    user_filter = UserFilter(request.GET)
    context = {
        'filter': user_filter
    }
    return render(request, "myapp/index.html", context)


def search_results(request):
    users = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=users)
    context = {
        'filter': user_filter
    }
    return render(request, "myapp/search.html", context)
