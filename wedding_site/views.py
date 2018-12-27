from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Greta og Steinar Åsmunds bryllup")