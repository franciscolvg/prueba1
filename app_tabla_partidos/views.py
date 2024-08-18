from django.shortcuts import render

#def lista_partidos(request):
    #partidos = ['PRM', 'FUPU']
    #return render(request, 'partidos.html', {'partidos': partidos})


def lista_partidos(request):
    return render(request, 'partidos.html')
