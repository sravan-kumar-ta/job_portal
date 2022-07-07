from django.contrib import messages
from django.shortcuts import redirect


def signin_required(fn):
    def wrapper(reqeust, *args, **kwargs):
        if reqeust.user.is_authenticated:
            return fn(reqeust, *args, **kwargs)
        else:
            messages.error(reqeust, 'Invalid session')
            return redirect('employer:sign-in')
    return wrapper
