from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def users(request):
    #pull data from third party rest api
    response = requests.get('http://127.0.0.1:8000/api-auth/users')
    #convert reponse data into json
    users = response.json()
    print(users)
    return HttpResponse("Users")
    pass