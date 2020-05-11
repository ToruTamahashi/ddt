from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from ddtapp.models import TestModel
from django.views.generic import ListView

def hellofunc(request):
    #値を渡す
    d = {
        'message': 'Sample message',
    }
    return render(request,'test.html',d)

class GetData(ListView):
    template_name = 'list.html'
    model = TestModel