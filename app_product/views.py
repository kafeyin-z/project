from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForms



def ekle(request):
    form = ProductForms()
    if request.method == 'POST':
        form = ProductForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            post_pre_commit = form.save(commit=False)
            post_pre_commit.author = request.user
            post_commit = post_pre_commit.save()
            messages.success(request, "İlanınız başarıyla oluşturuldu.")
            return HttpResponseRedirect(reverse('product-detay', kwargs={'pk': post_pre_commit.pk}))
    context = {'form': form}
    return render(request, 'product/ekle-guncelle.html', context=context)


def listele(request):
    posts = Product.objects.all()
    context = {'posts': posts}
    return render(request, 'product/listele.html', context=context)


def guncelle(request, pk):
    data = get_object_or_404(Product, pk=pk)
    form = ProductForms(instance=data)
    if request.method == 'POST':
        form = ProductForms(instance=data, data=request.POST, files=request.FILES)
        if form.is_valid():
            post_pre_commit = form.save(commit=False)
            post_pre_commit.author = request.user
            post_commit = post_pre_commit.save()
            messages.success(request, "İlanınız başarıyla güncelleştirildi.")
            return HttpResponseRedirect(reverse('product-detay', kwargs={'pk': post_pre_commit.pk}))
    context = {'form': form}
    return render(request, 'product/ekle-guncelle.html', context=context)


def sil(request, pk):
    post = get_object_or_404(Product, pk=pk)
    post.delete()
    messages.warning(request, "İlanınız silindi.")
    return HttpResponseRedirect(reverse('product-listele'))


def detay(request, pk):
    post = get_object_or_404(Product, pk=pk)
    context = {'post': post}
    return render(request, 'product/detay.html', context=context)


def anasayfa(request):
    return render(request, 'anasayfa.html')
