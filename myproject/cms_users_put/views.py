from django.shortcuts import render
from models import Pages
from models import Css
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context


@csrf_exempt
def servircss(request, recurso):
    print "CSS"
    if request.method == 'GET':
        try:
            css = Css.objects.get(name=recurso)
            return HttpResponse(css.page,content_type="text/css")
        except Css.DoesNotExist:
            return HttpResponseNotFound( recurso + " no encontrado")

    elif request.method == 'PUT':
            print "recurso" + recurso
            p = Css(name=recurso, page=request.body)
            p.save()
            return HttpResponse("Pagina guardada: " + request.body)

@csrf_exempt
def cms_users_put(request, recurso):
    print "CMS"   
    if request.method == 'GET':
        try:
            pages = Pages.objects.get(name=recurso)

             #Indicamos plantilla
            template = get_template("index.html")
            #Marcamos contexto:
            c = Context({'mensaje' : pages.page})
            renderizado = template.render(c)
            return HttpResponse(renderizado)

        except Pages.DoesNotExist:
            template = get_template("index.html")
            #Marcamos contexto:
            c = Context({'mensaje' : "Recurso no encontrado"})
            renderizado = template.render(c)
            return HttpResponseNotFound(renderizado)
    elif request.method == 'PUT':
 
        if  request.body.find('<body>') == -1:
            return HttpResponseNotFound("formato html erroneo</br>" +
                    "formato: <html><body>...texto...</body></html")


        lista = request.body.split('<body>')[1]
        to_save = lista.split('</body>')[0]

        p = Pages(name=recurso, page=to_save)
        p.save()
        return HttpResponse("<p>Pagina guardada: " + to_save +"</p>")
   
