from django.shortcuts import render


def index(request):
    return render(request, 'home_one.html')
def navabr(request):
    return render(request, 'header.html')
def footer(request):
    return render(request, 'footer.html')
def newindex(request):
    return render(request, 'index.html')