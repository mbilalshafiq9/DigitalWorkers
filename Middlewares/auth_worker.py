from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if not request.user.is_authenticated:
            messages.error(request, 'You need to login as Worker!')
            return redirect('login')
        elif request.user.role != 'worker':
            messages.error(request, 'You need to login as Worker!')
            return redirect('login')
        response = get_response(request)
        return response

    return middleware