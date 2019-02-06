from django.shortcuts import render, get_object_or_404, redirect
# from main.models import Children

from django.contrib.auth.decorators import login_required

from main.forms import UserForm, UserFormLast, IWMForm, IWM

from django.contrib.auth.models import User, Group

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse
from main.models import Tasks, Player, Developer, Game


def index(request):
    if request.method == 'GET':
        return HttpResponse('Hello world')


def signup(request):
    if request.user.is_authenticated:
        return redirect('main:index')
    return render(request, 'main/signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:index')
    return render(request, 'main/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:login')


def create(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        developer = False
        try:
            if request.POST['developer']:
                developer = True
        except KeyError:
            developer = False
        if username is not None and email is not None and password is not None:
            if not username or not email or not password:
                return render(request, 'main/signup.html', {'error': 'Please fill in all required fields'})
            if User.objects.filter(username=username).exists():
                return render(request, 'main/signup.html', {'error': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'main/signup.html', {'error': 'Email already exists'})
            user = User.objects.create_user(username, email, password)
            if developer:
                if Group.objects.filter(name='developers').exists():
                    dev_group = Group.objects.get(name='developers')
                else:
                    Group.objects.create(name='developers').save()
                    dev_group = Group.objects.get(name='developers')
                dev_group.user.user_set.add(user)
                Developer.objects.create(user=user).save()
            else:
                Player.objects.create(user=user).save()
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('main:index')
    else:
        return redirect('shop:singup')


def home(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('main:index')
        games = Game.objects.all()
        return render(request, 'main/home.html', {'games': games})
    else:
        return HttpResponse(status=500)


def login_user(request):
    pass


def catalog_view(request):
    pass


# @login_required(login_url='/auth/login')
# def home(request):
#     childs = Children.objects.all()
#     return render(request, 'index.html', {'childs': childs})
#
#
# def child_detail(request, child_id):
#     child = get_object_or_404(Children, id=child_id)
#     return render(request, 'child_detail.html', {'child': child})


# @login_required(login_url='/auth/login')
def home(request):
    return render(request, 'main/home.html', {})


def auth_registration(request):
    iwm_form = IWMForm()

    if request.method == 'POST':
        iwm_form = IWM(request.POST, request.FILES)

        if iwm_form.is_valid():
            iwm_form.save()

            login(request, authenticate(
                username = iwm_form.cleaned_data['username'],
                password = iwm_form.cleaned_data['password']
            ))

            return redirect(home)

    return render(request, 'auth/registration.html', {
        'iwm_form': iwm_form
    })
