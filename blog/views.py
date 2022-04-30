from django.db.models import Count , Q
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Blog , Author
from .forms import BlogForm
from django.core.paginator import Paginator

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def get_category_count():
    queryset = Blog.objects.values('categories__name').annotate(Count('categories__name'))
    return queryset

def updatePost(request, slug):
    post = Blog.objects.get(slug=slug)
    post_form = BlogForm()
    if request.method == "POST":
        post_form = BlogForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('blog')
    context = {'form': post_form}
    return render(request, 'blog/update.html' , context)

def deletePost(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect('blog')

    context = {'post': post}
    return render(request, 'blog/delete.html', context)

def createPost(request): 
    author = get_author(request.user)
    print(author)
    post_form = BlogForm(initial={'author':author})  
    if request.method == "POST":
        post_form = BlogForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('blog')
    context = {'form': post_form}
    return render(request, 'blog/create.html' , context)


def testPost(request): 
    post_form = BlogForm()  
    if request.method == "POST":
        post_form = BlogForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('blog')
    context = {'form': post_form}
    return render(request, 'blog/test.html' , context)






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
    post = Blog.objects.order_by('-created_date')
    paginator = Paginator(post, 5)
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
    category_count = get_category_count()
    latest_post = Blog.objects.order_by('-created_date')[:3]
    post_slug = Blog.objects.get(slug=slug)
    post = Blog.objects.get(slug=slug)
    context = {
        'slug': slug,
        'post':post,
        'latest': latest_post,
        'category_count': category_count,
    }
    return render(request, 'blog/post.html', context)