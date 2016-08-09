from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'zaakpay.views.index'),
	url(r'^posttozaakpay/$', 'zaakpay.views.posttozaakpay'),
	url(r'^response/$', 'zaakpay.views.response'),
)
