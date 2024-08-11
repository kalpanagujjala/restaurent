from django.shortcuts import render
from food.models import menu

# Create your views here.
def home(request):
    result=menu.objects.all()
    if request.method=='POST':
        no=(request.POST.get('price'))
        if menu.objects.filter(id=no).exists():
            a=menu.objects.get(id=no)
            return render(request,'index.html',{'res':result,'res2':a})
    
        return render(request,'index.html',{'res':result})

def itemadd(request):
    result=menu.objects.all()
    if request.method=="POST":
        dish=request.POST.get('food')
        price=request.POST.get('food_price')
        obj=menu(item=dish,cost=price)
        obj.save()
        return render(request,'form.html')
    return render(request,'form.html')