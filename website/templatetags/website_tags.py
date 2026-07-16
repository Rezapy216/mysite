from django import template
from blog.models import Post
register = template.Library()

@register.inclusion_tag('website/index-latestposts.html')
def index_latestposts(arg=6):
    posts = Post.objects.filter(status=1)
    return {'posts': posts}