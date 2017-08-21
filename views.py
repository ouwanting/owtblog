from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from owtblog.models import Blogpost


def Index(request):
    blog_list = Blogpost.objects.all() #获取Blogpost实例
    return render(request,'owtblog/index.html',{'blog_list':blog_list})

def topics(request):
    topics = Blogpost.objects.order_by('timestamp')
    context = {'topics':topics}
    return render(request,'owtblog/topics.html',context)
