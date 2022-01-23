from django.db.models import Count , Q
from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

def get_category_count():
    queryset = Blog.objects.values('categories__name').annotate(Count('categories__name'))
    return queryset


def blogSearch(request):
    category_count = get_category_count()
    latest_post = Blog.objects.order_by('-created_date')[:3]
    queryset = Blog.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(desc__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
        'latest': latest_post,
        'category_count': category_count,
    }
    return render(request, 'blog/search_results.html', context)
# Create your views here.
def blog(request):
    category_count = get_category_count()
    latest_post = Blog.objects.order_by('-created_date')[:3]
    post = Blog.objects.all()
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page')
    finaldata = paginator.get_page(page_number)
    totalpages = finaldata.paginator.num_pages
    context = {
        'post':finaldata,
        'lastpage' : totalpages,
        'totalpagelist' : [n+1 for n in range(totalpages)],
        'latest': latest_post,
        'category_count': category_count,
        }
    return render(request, 'blog/blog.html', context)

def post(request, slug):
    
    post_slug = Blog.objects.get(slug=slug)
    context = {
        'slug': slug,
        'post':post,
    }
    return render(request, 'blog/post.html', context)