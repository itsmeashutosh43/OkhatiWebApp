from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views


from . import views 

urlpatterns=[
	url('', include('pwa.urls')),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^form/$', views.formy, name='formy'),
	url(r'^home/$',views.home,name='home'),
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^myStore/',views.myStore,name='My Store'),

]




