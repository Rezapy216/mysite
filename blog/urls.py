from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [

    path('', blog_home_view, name='index'),
    path('<int:pid>', blog_single_view, name='single'),
    # path('post-<int:pid>', test)

]
