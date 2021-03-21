from django.shortcuts import render
from .models import Storage
import fnmatch, os, random
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

number_files = len(fnmatch.filter(os.listdir('/home/busyangels/busy-angels/static/img/'), '*.jpg'))
#number_files = len(fnmatch.filter(os.listdir('static/img/'), '*.jpg'))

def storage(request):
    template = 'document/storage.html'
    rand = random.randint(1, number_files)
    scraps = Storage.objects.all()

    context ={
        'rand':rand,
        'scraps':scraps,
    }

    return render(request, template, context)

class StorageAddView(CreateView):
    model = Storage
    fields = [
        'classify',
        'title',
        'desc',
        'url',
    ]

    success_url = reverse_lazy('my_storage')
    template_name_suffix = '_add'