from django.shortcuts import render, redirect
from .models import Photo, Category

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name =category)
    
    categories= Category.objects.all()
    context = {'categories':categories, 'photos':photos}
    return render(request, 'photo/gallery.html', context)

def viewphoto(request, pk):
    photos = Photo.objects.get(id=pk)    
    return render(request, 'photo/photo.html', {'photos':photos})

def addphoto(request):
    categories= Category.objects.all()
    
    if request.method == 'POST':
        data=request.POST
        images = request.FILES.getlist('images')
    
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )
        return redirect('gallery')
    
    context = {'categories':categories}
    return render(request, 'photo/add.html', context)
 