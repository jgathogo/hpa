from django.conf.urls import url

from . import views

app_name = 'cfp'
urlpatterns = [
    url(r'^$', views.cfp_home, name='home'),
    url(r'all-calls-for-proposals/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.CfPDetailView.as_view(), name='cfp_detail'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.CfPDetailView.as_view(), name='cfp_detail'),
    url(r'^(?P<pk>[0-9]+)/edit-cfp/$', views.edit_cfp, name='edit_cfp'),
]
