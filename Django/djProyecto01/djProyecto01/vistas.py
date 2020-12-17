from django.http import HttpResponse


def saludo(request):

    msjSaludo = '<html><body><h1><p style="color:red;">Hola World!</p></h1></body></html>'

    return HttpResponse(msjSaludo)


def despedida(request):

    msjDespedida = '<html><body><h1><p style="color:blue;">Nos veremos</p></body></h1></html>'

    return HttpResponse(msjDespedida)

