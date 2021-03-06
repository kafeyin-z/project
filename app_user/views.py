from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect, get_object_or_404

from .forms import GirisForm, KayitForm, ProfilForm
from .models import UserProfile


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


@login_required
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


@login_required
def profil(request):
    data = UserProfile.objects.filter(author=request.user)
    context = {'profil': data}
    return render(request, 'user/profil.html', context=context)


@login_required
def profil_degistir(request):
    data = get_object_or_404(UserProfile, author=request.user)
    form = ProfilForm(instance=data)
    if request.method == 'POST':
        form = ProfilForm(instance=data, data=request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author =request.user
            post.save()
    context = {'profil': form}
    return render(request, 'user/profil-guncelle.html', context=context)


@login_required
def sifre_degistir(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user-sifre')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'user/sifre_degistir.html', context=context)
