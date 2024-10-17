# Importa la función 'render' desde django.shortcuts.
# 'render' se usa para generar respuestas HTTP que contienen plantillas HTML (no lo estamos usando aún).
from django.shortcuts import render

# Importa 'HttpResponse' desde django.http.
# 'HttpResponse' se usa para devolver una respuesta HTTP con contenido simple, como texto o HTML.
from django.http import HttpResponse

# Define una vista llamada 'index', que toma un objeto 'request' como argumento.
# 'request' contiene toda la información de la solicitud HTTP que hace el cliente (como el navegador web).
def index(request):
    # Retorna una respuesta HTTP que contiene el texto plano "Hello world, esto es una encuesta."
    # Cuando alguien acceda a la URL asociada a esta vista, verá este mensaje en su navegador.
    return HttpResponse("Hello, world. You're at the polls index.")
