from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Texts
from triples.models import Triples
import numpy as np
import json
import os

# Create your views here.
def returnJson(data = None, errorCode = 0):
    if data is None:
        data = []
    return JsonResponse({'errorCode' : errorCode, 'data' : data})

def texts_list(request):
    texts = Texts.objects.order_by('-id')
    return returnJson([dict(text.body()) for text in texts])

def text(request, pk):
    if request.method == 'GET':
        text = Texts.objects.get(id=pk)
        return returnJson([dict(text.body())])

def create_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        text = Texts.objects.create(text=data['text'], created_by=data['username'], json_created=data['json_created'])
        #text.json_created = generate_json(data['text'])
        #text.json_created = {'text':'abc'}
        text.save()

        for triple in data['json_created']:
            Triples.objects.create(
                entity1=triple['entity1'],
                relationship=triple['relationship'],
                entity2=triple['entity2'],
            )

        return returnJson([dict(text.body())])
        
def delete_text(request, textId):
    username = request.user.username

    if request.method == 'DELETE':
        try:
            
            text = Texts.objects.get(id=textId)
            print(text.created_by)
            # print(username)
            if username == text.created_by:
                text.delete()
                texts = Texts.objects.all()
                return returnJson([dict(text.body()) for text in texts])

            else:
                return returnJson([], 400)
        except Texts.DoesNotExist:
            return returnJson([], 404)
