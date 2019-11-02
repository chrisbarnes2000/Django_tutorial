from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404

from .models import Event

# Create your views here.
def index(request):
    latest_event_list = Event.objects.order_by('-pub_date')[:5]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/detail.html', {'event': event})
