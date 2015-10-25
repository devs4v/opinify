from django.conf.urls import include, url
from views import PollsHome, ShowPoll, NewPoll, EditPoll, YourPoll, EditOptions

urlpatterns = [
	url(r'^$', PollsHome.as_view(), name="home"),
	url(r'^new$', NewPoll.as_view(), name="new"),
	url(r'^your$', YourPoll.as_view(), name="your"),
	url(r'^(?P<poll_id>[0-9]+)/$', ShowPoll.as_view(), name="show"),
	url(r'^(?P<poll_id>[0-9]+)/options$', EditOptions.as_view(), name="editoptions"),
	url(r'^(?P<poll_id>[0-9]+)/edit$', EditPoll.as_view(), name="edit"),
]