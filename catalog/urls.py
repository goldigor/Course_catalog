from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.course_list, name='course_list'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^course/new/', views.course_new, name='course_new'),
    url(r'^course/(?P<pk>\d+)/edit/$', views.course_edit, name='course_edit'),
    url(r'^course/(?P<pk>\d+)/delete/$', views.course_delete, name='course_delete'),
    url(r'^course/search/', views.course_search, name='course_search'),
]
