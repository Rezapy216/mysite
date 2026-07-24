from sqlite3 import connect
from unicodedata import category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, HttpResponse
from blog.models import Post
from website.models import Contact
from blog.forms import NameForm, ContactForm


def blog_home_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)

    if cat_name:
        posts = posts.filter(category__name=cat_name)

    if author_username:
        posts = posts.filter(author__username=author_username)

    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)

    except PageNotAnInteger:
        posts = posts.get_page(1)

    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)


def blog_single_view(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    next_post = posts.filter(id__gt=post.id).order_by('id').first()
    prev_post = posts.filter(id__lt=post.id).order_by('-id').first()
    context = {'post': post, 'next_post': next_post, 'prev_post': prev_post
               }
    return render(request, "blog/blog-single.html", context)


def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('done')
    form = ContactForm()
    return render(request, 'test.html', {'form': form})


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        if s := request.method == 'GET':
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
