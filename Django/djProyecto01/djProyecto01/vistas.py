from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def saludo(request):

    #msjSaludo = '<html><body><h1><p style="color:red;">Hola World!</p></h1></body></html>'

    doc_externo = open('D:/Local/Documentos/Programacion/GIT/Django/djProyecto01/djProyecto01/plantillas/saludo.html', encoding='utf-8-sig')
    # encoding='utf-8-sig' para eliminar simbolos raros al inicio de la Pagina Web

    plt = Template(doc_externo.read())
    doc_externo.close()

    doc_externo = loader.get_template('saludo.html')
    ctx = Context()
    msjSaludo = plt.render(ctx)

    return HttpResponse(msjSaludo)


def despedida(request):

    msjDespedida = '<html><body><h1><p style="color:blue;">Nos veremos</p></body></h1></html>'

    return HttpResponse(msjDespedida)

