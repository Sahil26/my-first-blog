from django.shortcuts import render
from  .models import Post

def post_list(request):
    posts = Post.objects.order_by('pub_date')
    return render(request,'blog/post_list.html', {'posts':posts})

