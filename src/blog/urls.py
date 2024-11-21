
from django.contrib import admin
from django.urls import path
from .views import index , article

urlpatterns = [
    path('index/',index,name="blog-index"),
    path('article-<str:number_article>/',article,name="blog-article"),

]