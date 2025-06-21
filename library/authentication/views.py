from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .models import CustomUser
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_books')
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user_obj = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                user_obj = None

            if user_obj and user_obj.check_password(password):
                login(request, user_obj)

                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('all_books')
            else:
                form.add_error(None, 'Invalid credentials')

    return render(request, "authentication/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'users/all_users.html', {'users': users})


@login_required
def user_details(request, user_id):
    user_obj = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'users/user_details.html', {'user_obj': user_obj})
