from django.http import HttpResponse

def saludo(request):

    return HttpResponse('Hola alumnos esta es nuestra primera pagina con DJango')

def despedida(request):

    return HttpResponse('Hasta luego alumnos de DJango')
