from django.shortcuts import render

# Create your views here.

def main_post(request) :
    return render(request,'polls/main_post.html',{})
