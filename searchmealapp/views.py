from django.shortcuts import render
import requests
import json
# Create your views here.
def get_meals(request):
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=' 
    #request na url
    req = requests.get(url)
    #pegando apenas o json sem metadata
    meals = req.json()
    #pegando meals como objeto e passando no contexto
    context = {'meals': meals['meals']}
    return render(request, "index.html", context)