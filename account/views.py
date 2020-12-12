from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage



# Create your views here.

def index(request):

   return render(request, 'index.html')

def service(request):
    
    return render(request, 'service.html')



def test(request):
    inp = request.POST.get('param')
    inp1 = request.POST.get('mykwrd1') 
    out = run([sys.executable,'C:\\Users\\DIVESH\\projects\\myproject\\account\\check.py',inp,inp1],shell=False,stdout=PIPE)
    print(out.stdout)

    return render(request, 'index.html',{'data':out.stdout})

def test1(request):
    inp = request.FILES['myfile']
    inp1 = request.POST.get('mykwrd')
    fs = FileSystemStorage()
    filename = fs.save(inp.name,inp)
    fileurl = fs.open(filename)
    templateurl = fs.url(filename)
    print(filename)
    print('file raw url',filename)
    print('file full url',fileurl)
    print('template url is ',templateurl)
    inp = run([sys.executable,'C:\\Users\\DIVESH\\projects\\myproject\\account\\check1.py',str(fileurl),str(filename),inp1],shell=False,stdout=PIPE)
    

    return render(request, 'index.html',{'raw_url':templateurl,'edit_url':inp.stdout})



