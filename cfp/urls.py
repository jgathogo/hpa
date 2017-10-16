from django.conf.urls import url

from . import views

app_name = 'cfp'
urlpatterns = [
    # add a home page here, change from index view
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'all-calls-for-proposals/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$',
        views.CfPDetailView.as_view(), name='cfp_detail'),
    url(r'^(?P<pk>[0-9]+)/edit-cfp/$', views.edit_cfp, name='edit_cfp'),
]
