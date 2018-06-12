from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.request
from addon import student_food
from addon import train
from addon import find_book
import time
from module.buttons import *
def JsonReturn(msg,buttons):
    return JsonResponse(
        {
        'message': {
            'text': msg,
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': buttons
        }
    })

def JsonLibraryReturn(msg,url,width,height):
    return JsonResponse(
        {
            'message': {
                'text': msg,
                'photo':{
                    'url': 'http://211.229.250.54/photo/' + str(url) + '.png',
                    'width': int(width),
                    'height': int(height)
            }},
            'keyboard': {
                'type': 'buttons',
                'buttons': reading_zone
            }
        }
    )

def JsonErrorReturn(msg):
    return JsonResponse(
        {
        'message': {
            'text': msg,
        },
        'keyboard': {
            'type': 'text',
        }
    })

def JsonMapReturn(msg,url,width,height):
    return JsonResponse(
        {
            'message': {
                'text': msg,
                'photo':{
                    'url': 'http://211.229.250.54/photo/' + str(url) + '.jpg',
                    'width': int(width),
                    'height': int(height)

            }},
            'keyboard': {
                'type': 'buttons',
                'buttons': building
                }
            }
        )
