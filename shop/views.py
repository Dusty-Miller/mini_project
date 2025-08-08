from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages

def shoplist(request):
    #db에서 query select * from post
    posts = Post.objects.all()
    return render(request,
                  template_name='shop/shoplist.html',
                  context={'posts':posts})


def shopdetail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,
                  'shop/shopdetail.html',
                  context={'post':post})

def shopmyPage(request):
    posts = Post.objects.all()
    return render(request,
                  'shop/shopmypage.html',
                  context={'posts':posts})

def create(request):
    if request.method == 'POST':
        #작성하다가 제출 버튼을 누른 경우
        postform = PostForm(request.POST,request.FILES)
        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.title = post1.title + ""
            postform.save()
            return redirect('/shop/')
    else: #get
        postform = PostForm()
    return render(request,
                  template_name="shop/postform.html",
                  context={'postform':postform})

def order_status(request):
    posts = Post.objects.all()
    return render(request,
                  'shop/order_status.html',
                  context={'posts':posts})

def order_history(request):
    posts = Post.objects.all()
    return render(request,
                  'shop/order_history.html',
                  context={'posts':posts})

def wishlist(request):
    posts = Post.objects.all()
    return render(request,
                  'shop/wishlist.html',
                  context={'posts':posts})

def contact(request):
    if request.method == "POST":
        commentform = CommentForm(request.POST, request.FILES)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.author = request.user if request.user.is_authenticated else None
            comment.save()  # ✅ 한 번만 저장 (루프 없음)
            messages.success(request, "문의가 등록되었습니다.")
            return redirect('contact')
    else:
        commentform = CommentForm()

    comments = Comment.objects.order_by("-created_date")  # ✅ 최신순
    return render(request, "shop/contact.html", {
        "commentform": commentform,
        "comments": comments,
    })

def contact_history(request):
    posts = Post.objects.all()
    return render(request,
                  'shop/contact_history.html',
                  context={'posts':posts})