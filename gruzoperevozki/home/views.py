import datetime

from django import utils
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


# Create your views here.
from .forms import MyBackend
from .models import User, Gruz


def user_not_auth_checker(function):
    # Если пользователь аутентифицирован, то все норм
    def check_auth(request):
        if request.user.is_authenticated:
            answer = function(request)
            return answer
        else:
            return redirect('login')

    return check_auth


def user_auth_checker(function):
    # Если пользователь не аутентифицирован, то логиниться
    def check_auth(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            answer = function(request)
            return answer

    return check_auth


@user_not_auth_checker
def home(request):
    if request.user.is_superuser:
        gruzi = Gruz.objects.all().values()
        return render(request, 'adminaccount/AdminAccount.html', {'gruzi': gruzi})
    else:
        return render(request, 'clientaccount/clientAccount.html')


@user_auth_checker
def authPage(request):
    return render(request, 'authorization/authorization.html')


@user_auth_checker
def authUser(request):
    if request.POST is not None:
        username = None
        password = None
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
        except Exception as e:
            print(repr(e))

        if username is not None and password is not None:
            user = User.objects.filter(username=username).values()

            if len(list(user)) != 0:
                authBack = MyBackend()
                doctor = authBack.authenticate(request, username=username, password=password)
                if doctor is not None:
                    login(request, doctor)
                return redirect('home')

    return redirect('login')


@user_not_auth_checker
def clientsList(request):
    if request.user.is_superuser:
        users = User.objects.all().values()
        return render(request, 'clientslist/ClientsList.html', {'users':users})


def clientPage(request, user_id):
    if request.user.is_superuser:
        userinfo = User.objects.filter(id=user_id).values().first()
        usergruz = Gruz.objects.filter(user_id=user_id)
        return render(request, 'aboutclient/AboutClient.html', {"user": userinfo,
                                                                'usergruz': usergruz})


@user_not_auth_checker
def clientGr(request):
    if not request.user.is_superuser:

        gruzi = Gruz.objects.filter(user_id=request.user.id).values()
        return render(request, 'clientsgruzi/ClientsGruzis.html', {"gruzi":gruzi})


@user_not_auth_checker
def sendGruz(request):
    if not request.user.is_superuser:
        if request.POST is not None:
            grus_name = request.POST.get('grus_name')
            if grus_name != '':

                Gruz.objects.create(user_id=request.user.id, name=grus_name)
    return redirect('home')


def sendGruzToClient(request, gruz_id):
    if request.user.is_superuser:
        print(gruz_id)

        Gruz.objects.filter(id=gruz_id).update(sent_to_position_date=str(datetime.date.today()))
    return redirect('clientsList')


@user_not_auth_checker
def logOut(request):
    logout(request=request)
    return redirect('home')

