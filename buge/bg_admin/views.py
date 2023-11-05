from django.shortcuts import render
from django.conf import settings


# Create your views here.
def AdminLogin(request):
    context = dict()
    context["form"]=LoginForm()
    return render(
        request,
        'bg_admin/login.html',
        context=context
    )