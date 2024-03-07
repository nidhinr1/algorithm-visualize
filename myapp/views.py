from .models import details
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
def display(request):
    data=details.objects.all()
    return render(request,"index.html",{'data':data})
def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def log(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('display')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def out(request):
    logout(request)
    return redirect('login')
def add(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        age1=request.POST.get('age')
        year1=request.POST.get('year')
        course1=request.POST.get('course')
        values=details(name=name1,age=age1,year=year1,course=course1)
        values.save()
        a="Student added!"
        return render(request,"add.html",{'a':a})
    else:
        return render(request,'add.html')
def delete(request):
    if request.method=="POST":
        ad=request.POST.get('admi')
        value=details.objects.filter(admissionno=ad)
        value.delete()
        a="Student deleted!"
        return render(request,"delete.html",{'a':a})
    return render(request,"delete.html")
def update(request):
    if request.method=="POST":
        name1=request.POST.get('name')
        age1=request.POST.get('age')
        year1=request.POST.get('year')
        course1=request.POST.get('course')
        values=details.objects.filter(name=name1).update(age=age1,year=year1,course=course1)
        return render(request,"update.html")
    else:
        id=request.GET['a']
        na=details.objects.filter(name=id)
        return render(request,"update.html",{'i':na})


