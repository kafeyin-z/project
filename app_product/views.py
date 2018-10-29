from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404

from .forms import ProductForms
from .models import Product


@login_required
def ekle(request):
    form = ProductForms()
    if request.method == 'POST':
        form = ProductForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "İlanınız başarıyla oluşturuldu.")
            return HttpResponseRedirect(reverse('product-detay', kwargs={'pk': post.pk}))
    context = {'form': form}
    return render(request, 'product/ekle-guncelle.html', context=context)


def listele(request):
    posts = Product.objects.all()
    context = {'posts': posts}
    return render(request, 'product/listele.html', context=context)


# FIXME: Güncellenecek post kaydeden kişi tarafından düzenlenebilecek şekilde ayarlanacak
@login_required
def guncelle(request, pk):
    data = get_object_or_404(Product, pk=pk)
    form = ProductForms(instance=data)
    if request.method == 'POST':
        form = ProductForms(instance=data, data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "İlanınız başarıyla güncelleştirildi.")
            return HttpResponseRedirect(reverse('product-detay', kwargs={'pk': post.pk}))
    context = {'form': form}
    return render(request, 'product/ekle-guncelle.html', context=context)


@login_required
def sil(request, pk):
    post = get_object_or_404(Product, pk=pk)
    post.delete()
    messages.warning(request, "İlanınız silindi.")
    return HttpResponseRedirect(reverse('product-listele'))


@login_required
def detay(request, pk):
    post = get_object_or_404(Product, pk=pk)
    context = {'post': post}
    return render(request, 'product/detay.html', context=context)


def anasayfa(request):
    return render(request, 'anasayfa.html')
