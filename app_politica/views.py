from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def lista_partidos(request):
    partidos = ["PRD", "PRM", "FUPU", "PLD"]
    return JsonResponse(partidos, safe=False)
