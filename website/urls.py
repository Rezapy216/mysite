
from django.urls import path
from website.views import *
app_name = 'website'
urlpatterns = [

    path("", index_view, name='index'),
    path("about", about_view),
    path("contact", contact_view, name='contact'),
    path('index', index_view),
    path('elements', elements_view)
]
