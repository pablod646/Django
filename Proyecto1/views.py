
from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):
    nombre = 'Juan'
    doc_externo = open('D:/Programing/Proyecto1/Proyecto1/plantillas/miplantilla.html')
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({'nombre_persona': nombre})
    documento = plt.render(ctx)
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse('chau puto')


def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    Fecha y hora actual: %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, edad, anio):
    periodo = anio - 2019
    edadfutura = edad + periodo
    documento = '<h2>En el año %s tendrás %s años</h2>' % (anio, edadfutura)
    return HttpResponse(documento)
