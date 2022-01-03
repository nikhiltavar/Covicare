from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
# Create your views here.
def blog(request):
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
        }
    return render(request, 'blog/blog.html', context)