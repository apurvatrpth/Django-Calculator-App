from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return render(response,"index.html",{'name':'this is a Calculator'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    op = request.POST['operation']

    if(op == '+'):
        res = val1 + val2
    elif(op == '-'):
        res = val1 - val2
    elif(op == '*'):
        res = val1 * val2
    else:
        res = val1/val2

    return render(request,"result.html",{'result': res})