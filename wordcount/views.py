from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

	
def count(request):
	fulltext = request.GET['fulltext']
	
	worldlist = fulltext.split()
	
	return render(request, 'count.html',{'fulltext':fulltext, 'count':len(worldlist)})
	
def about(request):
    return render(request, 'about.html')
	
	
