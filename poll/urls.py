from django.conf.urls import include, url
from views import PollsHome, ShowPoll, NewPoll, EditPoll, YourPoll

urlpatterns = [
	url(r'^$', PollsHome),
	url(r'^new$', NewPoll.as_view(), name="new"),
	url(r'^your$', YourPoll.as_view(), name="your"),
	url(r'^(?P<pk>[0-9]+)/$', ShowPoll.as_view(), name="show"),
	url(r'^(?P<pk>[0-9]+)/edit$', EditPoll.as_view(), name="edit"),
]