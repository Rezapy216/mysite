from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag(name='totalposts')
def hello():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts


@register.filter
def snippets(value, arg=9):
    return value[:arg] + '...'

@register.inclusion_tag('blog/latestposts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_time')[:arg]
    return {'posts': posts}


