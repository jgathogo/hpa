from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect

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


# def edit_cfp(request, pk):
#     cfp_inst = get_object_or_404(Cfp, pk=pk)

#     # If this is a POST request then process the Form data
#     if request.method == 'POST':
#         # Create a form instance and populate it with data from the request
#         # (binding):
#         form = EditCfPForm(request.POST)

#         # Check if the form is valid
#         if form.is_valid():
#             cfp_inst = form.cleaned_data['cfp_title']
#             cfp_inst.save()

#             # redirect to a new URL:
#             return HttpResponseRedirect('/thank-you/')

#     else:
#         form = EditCfPForm(initial={'cfp_title': Cfp.cfp_title})
#     return render(request, 'cfp/edit_cfp.html', {'form': form})
def edit_cfp(request, pk):
    cfp = get_object_or_404(Cfp, pk=pk)
    # form = EditCfPForm(instance=cfp)

    if request.method == "POST":
        form = EditCfPForm(request.POST, instance=cfp)
        if form.is_valid():
            cfp = form.save(commit=False)
            cfp.save()
            return redirect('/')
    else:
        form = EditCfPForm(instance=cfp)
    return render(request, 'cfp/edit_cfp.html', {'form': form})
