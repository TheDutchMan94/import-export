from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def home(request):
    blogs = Blog.objects.all()[:2]
    products = Product.objects.all()[:3]
    partners = Partner.objects.all()

    context = {
        'blogs':blogs,
        'products':products,
        'partners':partners
    }
    return render(request, 'index.html', context)

def aboutus(request):
    return render(request, 'about_us.html')

def contactus(request):
    if request.POST:
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            Contactus.objects.create(name=name, phone=phone, email=email, subject=subject, message=message)
            
            return redirect('home')
        except:
            return redirect('contact us')
    else:
        return render(request, 'contact.html')

def blog(request):
    cats = Blogcategory.objects.all()
    blogs = Blog.objects.all()

    context = {
        'cats':cats,
        'blogs':blogs
    }
    return render(request, 'blog.html', context)

def blogdetail(request, id):
    blog = Blog.objects.filter(id=id)

    context = {
        'blog':blog
    }
    return render(request, 'blogDetails.html', context)

def imppro(request, id):
    products = Product.objects.filter(subcategory__id=id)
    impname = Subcategory.objects.filter().first()
    context = {
        'products':products,
        'impname':impname
    }
    return render(request, 'import.html', context)

def exppro(request, id):
    products = Product.objects.filter(subcategory__id=id)
    exponame = Subcategory.objects.filter().first()
    
    context = {
        'products':products,
        'exponame':exponame
    }
    return render(request, 'import.html', context)