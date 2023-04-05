from django.shortcuts import render
from .code import *

def coder(request):
    if request.method == 'POST':
        ls = list(request.POST)
        if "crypto" in ls:
            messange = request.POST.get('messange')
            res, mes = code(messange)
            return render(request, 'C:/Users/KonVo/Desktop/Study/Django/vova/laba/rsaa/templates/index.html', {'mes': mes, 'res' : res})
    else:
        return render(request, 'C:/Users/KonVo/Desktop/Study/Django/vova/laba/rsaa/templates/index.html')

def pageNotFound(request, exception):
    return render(request, 'error404.html')
