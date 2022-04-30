from django.shortcuts import render
from .models import Hospital
from django.core.paginator import Paginator
from django.db.models import Count , Q

# Create your views here.
def hospital(request):
    
    latest_centres = Hospital.objects.order_by('-created_date')[:3]
    centre = Hospital.objects.order_by('-created_date')
    paginator = Paginator(centre, 5)
    page_number = request.GET.get('page')
    finaldata = paginator.get_page(page_number)
    totalpages = finaldata.paginator.num_pages
    context = {
        'centre':finaldata,
        'lastpage' : totalpages,
        'totalpagelist' : [n+1 for n in range(totalpages)],
        'latest': latest_centres,
        }
    
    return render(request, 'resources/resources.html', context)

def centreDetail(request, slug):
    latest_centre = Hospital.objects.order_by('-created_date')[:3]
    centre_slug = Hospital.objects.get(slug=slug)
    centre = Hospital.objects.get(slug=slug)
    context = {
        'slug': slug,
        'centre':centre,
        'latest': latest_centre,
    }
    return render(request, 'resources/centredetails.html', context)

def centreSearch(request):
    queryset = Hospital.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(desc__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
    }
    return render(request, 'resources/search_results.html', context)