from django.views.generic import TemplateView, View

class Homepage(TemplateView):
	""" the home page of the site """
	template_name = 'homepage.html'


class Signup(View):
	pass