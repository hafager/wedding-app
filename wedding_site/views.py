from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Marte og Håvards bryllup")
