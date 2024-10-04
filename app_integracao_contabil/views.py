from django.shortcuts import render

# Create your views here.

def integracao_contabil_view(request):
    return render(request, 'input/integracao_contabil.html')

def listagens_execucao_view(request):
    return render(request, 'input/listagens_execucao.html')