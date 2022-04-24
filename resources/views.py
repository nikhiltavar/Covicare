from django.shortcuts import render

# Create your views here.
def hospital(request):
    context = {}
    return render(request, 'resources/resources.html', context)