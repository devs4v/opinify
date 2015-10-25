from django.shortcuts import render
from django.views.generic import TemplateView, View


class PollsHome(TemplateView):
	""" PollsHome : show all polls """
	template_name = 'poll_home.html'

class ShowPoll(View):
	""" ShowPoll: show single poll by ID """
	template_name = 'poll_show.html'

class NewPoll(View):
	""" NewPoll : Create new poll """
	template_name = 'poll_new.html'

class EditPoll(View):
	""" EditPoll : edit and update poll """
	template_name = 'poll_edit.html'


class YourPoll(View):
	""" YourPoll : View all polls by the current user """