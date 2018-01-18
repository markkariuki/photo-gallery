from django.shortcuts import render
form django.http import HttpResponse

# Create your views here.
def Welcome(request):
    reutrn HttpResponse('welcome to my portfoio project')
