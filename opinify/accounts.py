# accounts.py
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect, render


class Login(View):
	def post(self, request):
		username = request.POST['username'].strip()
	    password = request.POST['password'].strip()
	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            return redirect('/')
	        else:
	            messages.error(request, 'Your account is disabled. Please check your email')
	            return redirect('/login')
	    else:
	        # Return an 'invalid login' error message

class Logout(View):
	def get(self, request):
		logout(request, user)
		return redirect('/')


class Signup(View):
	def get(self, request):
		return render