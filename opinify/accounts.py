# accounts.py
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect, render
from forms import SignupForm, LoginForm
from django.contrib.auth.models import User


class Login(View):
	login_template = 'login.html'
	
	def get(self, request):
		form = LoginForm()
		return render(request, Login.login_template, {'form':form})

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/')
				else:
					messages.error(request, 'Your account is disabled. Please check your email.')
			else:
				messages.error(request, 'Invalid username or password!')
			
		return render(request, Login.login_template, {'form': form})

class Logout(View):
	def get(self, request):
		logout(request)
		return redirect('/')


class Signup(View):
	signup_template = 'signup.html'
	def get(self, request):
		form = SignupForm()
		return render(request, Signup.signup_template, {'form': form})

	def post(self, request):
		form = SignupForm(request.POST)
		if form.is_valid():

			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password'],
				email = form.cleaned_data['email'],
				first_name = form.cleaned_data['first_name'],
				last_name = form.cleaned_data['last_name'],
				)
			user.is_active = True
			user.save()

			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request, user)
			return redirect('/')
		else:
			return render(request, Signup.signup_template, {'form': form})
