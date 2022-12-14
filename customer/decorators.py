from django.shortcuts import redirect
from django.contrib import messages
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request, *args, **kwargs)
        else:
            messages.error(request, "You must Login")
            return redirect("signin")
    return wrapper