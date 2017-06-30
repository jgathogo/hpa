from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Cfp, Donor, Theme, Zone
from .forms import EditCfPForm


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


def edit_cfp(request, pk):
    cfp_inst = get_object_or_404(Cfp, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        # (binding):
        form = EditCfPForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            cfp_inst.due_back = form.cleaned_data['cfp_title']
            cfp_inst.save()

            #redirect to a new URL:
            # Read MDN tutorial then come back, 30 June 2017
            
