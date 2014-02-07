from django.conf.urls import url,patterns,include

urlpatterns = patterns('',
	url(r'^about-us/','blog.views.aboutus'),
	url(r'^$','blog.views.index',name='home'),
	)