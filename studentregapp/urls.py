from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('reg',views.reg,name='reg'),
    path('studentlist',views.studentlist,name='studentlist'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_details/<int:pk>',views.edit_details,name='edit_details'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('viewstudents/<int:pk>',views.viewstudents,name='viewstudents'),
]