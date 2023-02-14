
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseNotFound
from task.models import Car, tasks

########################################################################################################################



def ex_login(request: HttpRequest)->HttpResponse:
    return render(request, 'login_page.html')

def ex_list(request: HttpRequest)->HttpResponse:
    ctx = {'object_list': tasks}
    return render(request, 'list_page.html', ctx)

def ex_reg(request: HttpRequest)->HttpResponse:
    return render(request, 'block3.html')

def pageNotfound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def task_list(request: HttpRequest, id: int)->HttpResponse:
    for x in tasks:
        if x['id'] == id:
            return render(request, 'list_page.html', {'obj':x})
    raise Http404

def ex_task_view(request: HttpRequest)->HttpResponse:
    ctx = {'object_list': Car.objects.all()
           }
    h = {'f': '2', 'e': '3'}
    return render(request, 'example_list.html', ctx)

def ex_task_detail_view(request: HttpRequest, pk: int)->HttpResponse:
    try:
        task = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        raise Http404('not found')
    ctx = {'object_list': Car.objects.first()
           }
    return render(request, 'example_det_list.html', ctx)