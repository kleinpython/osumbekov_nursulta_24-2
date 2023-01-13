from django.shortcuts import HttpResponse, redirect
import datetime

def main_view(request):
    if request.method == 'GET':
        return HttpResponse('hello! its my first view')

def redirect_to_youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com/')

def project(request):
    if request.method == 'GET':
        return HttpResponse('Hi! its my first project')

def good_bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
def date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().date)