import json
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
   # this will most likely need to be pointed elsewhere
    return render(request, "registration/register", {"form": form})


def logout_view(request):
    logout(request)


@login_required
def home(request):
    return HttpResponse('Home Page')

@csrf_exempt
def teacher_respose(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_cart = Exercise.objects.create(
            name=request.user.username,
            topic=data['topic'],
            difficulty=data['difficulty'],


        )
        mive = {
            'name': new_cart.name,
            'topic': new_cart.topic,
            'difficulty': new_cart.difficulty,
        }
        return HttpResponse(json.dumps(mive), content_type='application/json')



@csrf_exempt
def student_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_cart = Cart.objects.create(
            owner=request.user.username,
            title=data['title'],
            image=data['image_url'],
            price=data['price']

        )
        mive = {
            'owner': new_cart.owner,
            'title': new_cart.title,
            'image': new_cart.image,
            'price': new_cart.price
        }
        return HttpResponse(json.dumps(mive), content_type='application/json')
