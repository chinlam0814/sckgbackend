from django.shortcuts import render
from django.http import JsonResponse
from .models import Triples
import json
import os

# Create your views here.
def returnJson(data = None, errorCode = 0):
    if data is None:
        data = []
    return JsonResponse({'errorCode' : errorCode, 'data' : data})

# get all triples
def triples_list(request):
    if request.method == 'GET':
        triples = Triples.objects.all()
        return returnJson([dict(triple.body()) for triple in triples])