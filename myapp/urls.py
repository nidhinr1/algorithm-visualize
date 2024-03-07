from django.urls import path
from . import views
urlpatterns=[
    path("",views.display,name="display"),
    path("add",views.add,name="add"),
    path("delete",views.delete,name="delete"),
    path("update",views.update,name="update"),
    path('login/', views.log, name='login'),
    path('signup/', views.sign, name='signup'),
    path('logout/', views.out, name='logout'),
]