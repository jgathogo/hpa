from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render

from .models import Cfp, Donor, Theme, Zone


def cfp_home(request):
    return render(request, 'cfp/cfp_home.html')


class IndexView(generic.ListView):
    template_name = 'cfp/index.html'
    context_object_name = 'all_cfps_list'

    def get_queryset(self):
        return Cfp.cfp.order_by('closing_date')


class CfPDetailView(generic.DetailView):
    model = Cfp
    template_name = 'cfp/cfp_detail.html'
