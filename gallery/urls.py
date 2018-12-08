from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    # landing page
    url('^$',views.gallery,name = 'gallery'),
    #search results page 
    url(r'^search/', views.search_results, name='search_results'),
    # link to the image details
    url(r'^image/(\d+)',views.image,name='image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)