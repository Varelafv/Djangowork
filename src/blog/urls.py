
from django.contrib import admin
from django.urls import path
from .views import index , article_01,article_02,article_03

urlpatterns = [
    path('index/',index,name="blog-index"),
    path('article-01/',article_01,name="blog-article01"),
    path('article-02/', article_02, name="blog-article02"),
    path('article-03/', article_03, name="blog-article03"),

]