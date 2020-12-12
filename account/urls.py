from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('service', views.service, name='service'),
    path('test', views.test, name='test'),
    path('test1', views.test1, name='test1'),
    

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

