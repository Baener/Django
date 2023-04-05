from django.http import HttpResponseNotFound
from django.shortcuts import render
from .vova import *

def show(request):
    if request.method == 'POST':
        ls = list(request.POST)
        if "encode" in ls:
            num = request.POST.get('num')
            num1 = request.POST.get('num1')
            num2 = request.POST.get('num2')
            result = code(num, num1, num2)
            return render(request, 'index.html', {'result': result})
    else:
        return render(request, 'index.html')

def pageNotFound(request, exception):
    return render(request, 'error404.html')
