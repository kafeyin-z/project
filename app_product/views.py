from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .models import Product
from .forms import ProductForms



def ekle(request):
    form = ProductForms()
    if request.method == 'POST':
        form = ProductForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse('product-detay', kwargs={'pk': post.pk}))
    context = {'form': form}
    return render(request, 'product/ekle-guncelle.html', context=context)


def listele(request):
    posts = Product.objects.all()
    context = {'posts': posts}
    return render(request, 'product/listele.html', context=context)


def guncelle(request, pk):
    data = Product.objects.get(pk=pk)
    form = ProductForms(instance=data)
    if request.method == 'POST':
        form = ProductForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse('product-detay', kwargs={'pk': post.pk}))
    context = {'form': form}
    return render(request, 'product/ekle-guncelle.html', context=context)


def sil(request, pk):
    post = get_object_or_404(Product, pk=pk)
    post.delete()
    return HttpResponseRedirect(reverse('product-listele'))


def detay(request, pk):
    post = get_object_or_404(Product, pk=pk)
    context = {'post': post}
    return render(request, 'product/detay.html', context=context)
