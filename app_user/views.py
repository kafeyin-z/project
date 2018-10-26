from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import GirisForm, KayitForm


def giris(request):
    form = GirisForm(data=request.POST or None)
    context = {'form': form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('product-listele'))
        else:
            context = {'form': form}
    return render(request, 'user/giris.html', context=context)


def cikis(request):
    logout(request)
    return HttpResponseRedirect(reverse('product-listele'))

# TODO: Kullanıcı adı email olarak düzenlenecek, username olarak görünen yerler Ad Soyad şeklinde düzenlenecek.
# FIXME: Giriş yapmış kullanıcı kayıt sayfasından tekrar kayıt yaptırabiliyor
def kayit(request):
    form = KayitForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newuser = User(username=username)
        newuser.set_password(password)
        newuser.save()

        login(request, newuser)
        return HttpResponseRedirect(reverse('product-listele'))
    context = {'form': form}
    return render(request, 'user/kayit.html', context=context)
