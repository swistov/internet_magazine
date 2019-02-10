from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from shop.models import Game, Developer, Player,Transaction
# Create your views here.


def index(request):
    if request.method == "GET":
        user = request.user
        if not request.user.is_authenticated:
            return redirect("shop:home")
        if user.groups.filter(name="developers").count() != 0:
            return redirect("shop:developer")
        transactions = Transaction.objects.filter(player=user.player.id)
        purchased_games = []
        for transaction in transactions:
            purchased_games.append(transaction.game)
        return render(request, "shop/index.html", {"user":user, "purchased_games":purchased_games})


def signup(request):
    if request.user.is_authenticated:
        return redirect("shop:index")
    return render(request, 'shop/signup.html')


def logout_view(request):
    logout(request)
    return redirect("shop:login")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("shop:index")
    return render(request, 'shop/login.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if not username or not password:
            return render(request, "shop/login.html", {"error":"One of the fields was empty"})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("shop:index")
        else:
            return render(request, "shop/login.html", {"error":"Wrong username or password"})
    else:
        return redirect("shop:index")


def home(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("shop:index")
        games = Game.objects.all()
        return render(request, "shop/home.html", {"games":games})
    else:
        return HttpResponse(status=500)


def create(request):
    if request.method == "POST":
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
                return render(request, "shop/signup.html", {"error": "Please fill in all required fields"})
            if User.objects.filter(username=username).exists():
                return render(request, "shop/signup.html", {"error": "Username already exists"})
            elif User.objects.filter(email=email).exists():
                return render(request, "shop/signup.html", {"error": "Email already exists"})
            user = User.objects.create_user(username, email, password)
            if developer:
                if Group.objects.filter(name="developers").exists():
                    dev_group = Group.objects.get(name="developers")
                else:
                    Group.objects.create(name='developers').save()
                    dev_group = Group.objects.get(name='developers')
                dev_group.user_set.add(user)
                Developer.objects.create(user=user).save()
            else:
                Player.objects.create(user=user).save()
            user.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("shop:index")

    else:
        return redirect("shop:signup")


def catalog_view(request):
    pass


def play_game(request, game_id):
    pass


def developer_view(request):
    pass


def search(request):
    pass


def publish(request):
    pass


def developers_games(request):
    pass


def edit_game(request, game_id):
    pass
