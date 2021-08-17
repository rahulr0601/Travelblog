from django.urls import path
from . import views
urlpatterns = [
    path('', views.fun, name='fun'),
    path('',views.blog,name='blog'),
    path('add', views.addition, name='add'),
    path('update_blog/', views.update_blog, name='update_blog'),

]