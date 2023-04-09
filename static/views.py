from django.shortcuts import render

from static.models import Destination
from .models import Destination
# Create your views here.
def index(request):

    # dest1 = Destination()
    # dest2 = Destination()
    # dest3 = Destination()

    # dest1.name = "Purse"
    # dest1.desc = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # dest1.img = 'img-3.png'
    # dest1.book = False

    # dest2.name = "Mobile"
    # dest2.desc = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
    # dest2.img = 'img-4.png'
    # dest2.book = True

    # dest3.name = "Cars"
    # dest3.desc = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
    # dest3.img = 'img-5.png'
    # dest3.book = False

    # dests = [dest1,dest2,dest3]

    dests = Destination.objects.all()
    return render(request,'index.html', {'dests':dests,})
