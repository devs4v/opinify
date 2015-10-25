from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from models import Poll, Options, Vote
from forms import PollForm, OptionForm

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class PollsHome(LoginRequiredMixin, TemplateView):
	""" PollsHome : show all polls """
	template_name = 'poll_home.html'

	def get(self, request):
		polls = Poll.objects.order_by('-created')
		return render(request, PollsHome.template_name, {'polls': polls})

class YourPoll(LoginRequiredMixin, View):
	""" YourPoll : View all polls by the current user """
	template_name = 'poll_your.html'

	def get(self, request):
		polls = Poll.objects.filter(creator=request.user)
		return render(request, YourPoll.template_name, {'polls':polls})

class ShowPoll(LoginRequiredMixin, View):
	""" ShowPoll: show single poll by ID """
	template_name = 'poll_show.html'
	
	def get(self, request, poll_id):
		poll = get_object_or_404(Poll, pk=poll_id)
		options = poll.options_set.all()
		return render(request, ShowPoll.template_name, {'poll': poll, 'options':options})


class NewPoll(LoginRequiredMixin, View):
	""" NewPoll : Create new poll """
	template_name = 'poll_new.html'

	def get(self, request):
		form = PollForm()
		return render(request, NewPoll.template_name, {'form': form})

	def post(self, request):
		form = PollForm(request.POST)
		if form.is_valid():
			import datetime
			from django.utils import timezone

			new_poll = form.save(commit=False)
			new_poll.expires = timezone.now() + datetime.timedelta(hours=48)
			new_poll.creator = request.user
			new_poll.save()
		else:
			return render(request, NewPoll.template_name, {'form': form})

		return redirect('poll:show', pk=new_poll.id) 


class EditPoll(LoginRequiredMixin, View):
	""" EditPoll : edit and update poll """
	template_name = 'poll_edit.html'

	def get(self, request, poll_id):
		user_polls = Poll.objects.filter(creator=request.user)
		poll = get_object_or_404(Poll, pk=poll_id)
		form = PollForm(instance=poll)
		return render(request, EditPoll.template_name, {'form':form, 'edit': True})

	def post(self, request, poll_id):
		user_polls = Poll.objects.filter(creator=request.user)
		poll = get_object_or_404(Poll, pk=poll_id)
		form = PollForm(request.POST, instance=poll)
		if form.is_valid():
			poll_save = form.save()
		else:
			return render(request, EditPoll.template_name, {'form':form, 'edit': True})

		return redirect(request, reverse('poll:show', poll_id=new_poll.id), {'form':form})

class EditOptions(LoginRequiredMixin, View):
	""" EditOptions : edit and update various options """
	template_name = 'options_edit.html'

	def get(self, request, poll_id):
		user_polls = Poll.objects.filter(creator=request.user)
		poll = get_object_or_404(Poll, pk=poll_id)
		form = PollForm(instance=poll)

		options = poll.options_set.all()
		if options:
			options_form = [OptionForm(instance=option) for option in options]
		else:
			options_form = None

		return render(request, EditOptions.template_name, {'poll':poll, 'options_form':options_form})

