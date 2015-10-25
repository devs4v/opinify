# forms.py - Poll
from django import forms
from models import Poll, Options

class PollForm(forms.ModelForm):
	class Meta:
		model = Poll
		fields = ('title',)

class OptionForm(forms.ModelForm):
	class Meta:
		model = Options
		fields = ('label',)