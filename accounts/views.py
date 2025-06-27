from django.http import Http404
from django.contrib.auth import get_user
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def register(request):
    user = get_user(request)
    if user.is_authenticated:
        raise Http404("Not Found")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optional: assign permission or group
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def custLoginView(request):
    user = get_user(request)
    if user.is_authenticated:
        return redirect("/")
    else:
        return (LoginView.as_view())(request)

def custLogoutView(request):
    user = get_user(request)
    if user.is_authenticated and request.method == "POST":
        return (LogoutView.as_view())(request)
    else:
        raise Http404("Not Found")

def login_csrf_failure(request, reason=""):
    # Optional: You can log the reason
    # print(f"CSRF failed because: {reason}")
    return redirect('login')

        