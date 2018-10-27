from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, reverse

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
            messages.success(request, "Tebrikler başarıyla giriş yaptınız.")
            return HttpResponseRedirect(reverse('product-listele'))
        else:
            context = {'form': form}
    return render(request, 'user/giris.html', context=context)


def cikis(request):
    logout(request)
    messages.warning(request, "Sistemden çıkış yapıldı.")
    return HttpResponseRedirect(reverse('product-listele'))


# TODO: Kullanıcı adı email olarak düzenlenecek, username olarak görünen yerler Ad Soyad şeklinde düzenlenecek.
def kayit(request):
    user_auth = get_user(request)
    if user_auth.is_authenticated:
        messages.success(request, "Giriş yapılmış durumda tekrar kayıt olamazsınız.")
        return HttpResponseRedirect(reverse('anasayfa'))
    form = KayitForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newuser = User(username=username)
        newuser.set_password(password)
        newuser.save()

        login(request, newuser)
        messages.success(request, "Tebrikler başarıyla üyelik kaydınız oluşturuldu.")
        return HttpResponseRedirect(reverse('product-listele'))
    context = {'form': form}
    return render(request, 'user/kayit.html', context=context)


def profil(request):
    user_auth = get_user(request)
    if user_auth.is_authenticated:
        messages.success(request, "Kullanıcı giriş yapmış.")
    else:
        messages.success(request, "Giriş yapılmamamış.")
    return render(request, 'anasayfa.html')
