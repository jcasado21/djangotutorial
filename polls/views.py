# Importa la función 'render' desde django.shortcuts.
# 'render' se usa para generar respuestas HTTP que contienen plantillas HTML (no lo estamos usando aún).
from django.shortcuts import render
from django.http import Http404

# Importa 'HttpResponse' desde django.http.
# 'HttpResponse' se usa para devolver una respuesta HTTP con contenido simple, como texto o HTML.
from django.http import HttpResponse
from django.template import loader


from .models import Question

# Define una vista llamada 'index', que toma un objeto 'request' como argumento.
# 'request' contiene toda la información de la solicitud HTTP que hace el cliente (como el navegador web).
def index(request):
    # Retorna una respuesta HTTP que contiene el texto plano "Hello world, esto es una encuesta."
    # Cuando alguien acceda a la URL asociada a esta vista, verá este mensaje en su navegador.
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

#La función render() toma el objeto de la solicitud como su primer argumento, un nombre de plantilla como su segundo argumento 
# y un diccionario como su tercer argumento opcional. La función devuelve un objeto HttpResponse de la plantilla que se 
# ha proporcionado representada con el contexto dado.

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})