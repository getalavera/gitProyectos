from django.http import HttpResponse
import datetime

def saludo(request):

    documento = '<html><body><h1>Hola alumnos esta es nuestra primera pagina con DJango</h1></body></html>'

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse('Hasta luego alumnos de DJango')

def dameFecha(request):

    fecha_actual = datetime.datetime.now()

    documento = '<html><body><h1>Fecha y hora actuales %s </h1></body></html>' % fecha_actual

    return HttpResponse(documento)