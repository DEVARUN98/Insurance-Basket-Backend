from django.shortcuts import render
from django.http import HttpResponse

def companies(request):
    companies = [
        {'id':1,'name':"insurance"}
        
    ]
    print("ggggggggggggggggggggggggggggggggggggggggggg",request.data)
    return HttpResponse(companies)
