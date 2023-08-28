from django.shortcuts import render

def index_view(request):
    #context = {'languages':[], 'edgucations':[],'skills':[], 'projects':[], 'about':[], 'contact':[]}
    return render(request,'index.html')
# Create your views here.
