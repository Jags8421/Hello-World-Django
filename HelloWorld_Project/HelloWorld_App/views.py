from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    # Handler to return Hello World! Json Response.
    return JsonResponse({'Message': 'Hello World!'})

    # return HttpResponse('Hello World!'), To return a HTTP Response, but we need to return a Json response as per the question.