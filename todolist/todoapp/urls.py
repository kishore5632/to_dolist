from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',task_view,name="task_view"),
    path('cdelete/<int:id>',cdelete,name="cdelete"),
    path('delete/<int:id>',delete,name="delete"),
    path('detail',detail,name="detail"),
    path('edit/<int:id>',edit,name="edit"),
    path('redirect',redirect,name="redirect")

]