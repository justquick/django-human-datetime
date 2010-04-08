from django.shortcuts import render_to_response
from humandt.fields import HumanDateTimeField, HumanTimeField, HumanDateField
from django.forms import Form
from django.template import RequestContext

class ExampleForm(Form):
    datetime = HumanDateTimeField(required=False)
    time = HumanTimeField(required=False)
    date = HumanDateField(required=False)

def example(request):
    dates = None
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            dates = form.cleaned_data
    else:
        form = ExampleForm()
    return render_to_response('example.html', {
        'form': form,
        'dates': dates,
        'input': request.POST.copy(),
    }, context_instance=RequestContext(request))    
