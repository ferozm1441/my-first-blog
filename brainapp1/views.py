from django.shortcuts import render

def hello(request):
   return render(request, "brainapp1/template/hello.html", {})