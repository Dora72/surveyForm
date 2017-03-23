from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)


def index(request):
    print ('*'*100)
    return render(request,"apps/first_app/index.html")