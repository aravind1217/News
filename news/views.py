from django.shortcuts import render

import requests


def home(request):
	url = f' https://newsapi.org/v2/top-headlines?country=us&apiKey=ae4c78377057454ebe13a7f781f16a32'
	response = requests.get(url)
	data = response.json()
	articles = data['articles']

	context ={
	  "articles":articles
	}
	return render(request,'index.html',context)

	