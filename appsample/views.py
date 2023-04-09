from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_context = {
        "name" : "Jhon",
        "num" : 17,
        "list" : [123,456,789,"abc",112,113]
    }
    return render(request,'home.html',my_context)


def add(request):

    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2

    return render(request,'result.html',{'result':res})
