from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'var1':'hello world','num1':1500}
    return render(request, 'basic_app/index.html', context=context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative.html')
