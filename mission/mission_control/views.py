from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# # Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect("home")
#     else:
#         form = UserCreationForm()
#     # this will most likely need to be pointed elsewhere
#     return render(request, "registration/register", {"form": form})
#
#
# def logout_view(request):
#     logout(request)
#
#
# @login_required
# def home(request):
#   return HttpResponse('Home Page')

