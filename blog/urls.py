from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls import include
from mysite import settings
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),


	url(r'^ckeditor/', include('ckeditor.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)