from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import treasureGram
from .froms import treasureForm
from django.views import generic

# Create your views here.
class homeindex(generic.ListView):
    template_name = 'treasures/home.html'
    context_object_name = 'all_treasures'

    def get_queryset(self):
        return  treasureGram.objects.all()


def detail(request, val):
    treasure = treasureGram.objects.get(id =val)
    return render(request, 'treasures/detail.html', {'treasure': treasure})

def add_new(request):
    if request.method == 'POST':
        form = treasureForm(request.POST)
        if form.is_valid():
            treasure = form.save()
            treasure.save()
            return redirect('/')

    else:
        form = treasureForm()
        return render(request, 'treasures/new_treasure.html', {'form':form})

def edit_treasure(request, val):
    treasure = get_object_or_404(treasureGram, pk=val)
    if request.method=='POST':
        form = treasureForm(request.POST, instance=treasure)
        if form.is_valid():
            treasure = form.save()
            treasure.save()
            return redirect('treasures:detail', val=treasure.pk)
    else:
        form = treasureForm(instance=treasure)
        return render(request,'treasures/edit_treasure.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email_id']
        password = request.POST['password']

        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
        user.save()
        print("user created")
        return redirect('/')

    else:
         return render(request, 'treasures/signup.html')


def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        from django.contrib import auth
        user = auth.authenticate(username=username1, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return HttpResponse('<h1 class="alert alert-success">incorrect password or username</h1>')

    else:
        return render(request,'treasures/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')