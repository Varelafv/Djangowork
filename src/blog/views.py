from django.shortcuts import render

# Create your views here.
def index (request ):
    return render(request,"blog/index.html")

def article(request,number_article):
    if number_article in ["01","02","03"] :
        return render(request,f"blog/article_{number_article}.html")
    else :
        return render(request, f"blog/article_not_found.html")
