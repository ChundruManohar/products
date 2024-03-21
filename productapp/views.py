from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product,Category,Comment
from .forms import ProductForm,CommentForm
from datetime import datetime
# Create your views here.
@login_required(login_url='login/')
def Showproducts(request):
    
    catgeory = request.GET.get('catgeory')
    if catgeory==None:
        product = Product.objects.order_by('-price').filter(is_published=True)
    else:
        product=Product.objects.filter(category__name=catgeory)
    
    page_num = request.GET.get("page")
    paginator = Paginator(product, 3)
    
    
    try:
        product = paginator.page(page_num)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
        
    categories = Category.objects.all()
    '''no= Product.objects.count()
    print(no)'''
    context= {
        'product':product,
        'categories':categories,
    }
    
    return render(request,'showproduct.html',context)
@login_required(login_url='showproduct')
def productdetails(request,pk):
    products = Product.objects.get(id = pk)
    context = {
        'products':products,
    }
    return render(request,'productdetails.html',context)
@login_required(login_url='showproduct')
def addproduct(request):
    form = ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('showproduct')
            
    context = {
        'form':form,
    }
    return render(request,'addproduct.html',context)
    
@login_required(login_url='showproduct')
def updateproduct(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showproduct')

    context = {
        'form':form,
    }
    return render(request,'updateproduct.html',context)
    
@login_required(login_url='showproduct')
def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showproduct')

@login_required(login_url='showproduct')
def searchbar(request):
    if request.method=="GET":
        search = request.GET.get('search')
        if search:
            product = Product.objects.filter(name__icontains=search)
            return render(request,'search.html',{'product':product})
        else:
            print('no information')
            return request(request,'search.html')
        
def add_comment(request, pk):
    Products = Product.objects.get(id=pk)

    form = CommentForm(instance=Products)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=Products)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=Products, commenter_name=name, comment_body=body, date_add =datetime.now())
            c.save()
            return redirect('showproduct')
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    


    context = {
        'form': form
    }

    return render(request, 'comment.html', context)