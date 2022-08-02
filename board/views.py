from django.shortcuts import render, redirect
from .models import Board, Reply
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get("page", 1)
    kw = request.GET.get("kw", "")
    cate = request.GET.get("cate", "")

    if kw:
        if cate == "sub":
            bset = Board.objects.filter(subject__startswith = kw)
        elif cate == "wri" :
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                bset = Board.objects.filter(writer= u)
            except:
                bset = Board.objects.none()
        elif cate == "con" :
            bset = Board.objects.filter(content__contains= kw)
        else:
            bset = Board.objects.none()
    else:
        bset = Board.objects.all()

    pag = Paginator(bset.order_by("-pubdate"), 10)
    obj = pag.get_page(page)

    context = {
        "bset" : obj,
        "kw" : kw,
        "cate" : cate,
    }
    return render(request, "board/index.html", context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    return render(request, "board/detail.html", {"b" : b, "rset" : r})

def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.user == b.writer:
        b.delete()
    else:
        pass    # 협박을 해줘야 다시 시도를 안 함
    return redirect("board:index")

def create(request):
    if request.method == "POST":
        r = request.POST
        Board(subject=r.get("sub"), writer=request.user, content=r.get("con"), pubdate=timezone.now()).save()
        return redirect("board:index")
    return render(request, "board/create.html")

def update(request, bpk):
    b = Board.objects.get(id=bpk)
    
    if request.user == b.writer:
        if request.method == "POST":
            b.subject = request.POST.get("sub")
            b.content = request.POST.get("con")
            b.save()
            return redirect("board:detail", bpk)
    else:
        pass    # 해킹에 대한 협박은 단호해야 하느니라
        return redirect("board:index")

    return render(request, "board/update.html", {"b" : b})

def deleteReply(request, bpk, rpk):
    r = Reply.objects.get(id=rpk)

    if request.user == r.replyer:
        r.delete()
        return redirect("board:detail", bpk)
    
    # 해킹 법규!
    return redirect("board:index")

def creply(request, bpk):
    Reply(board=Board.objects.get(id=bpk), replyer=request.user, comment=request.POST.get("rcomm")).save()

    return redirect("board:detail", bpk)

def ureply(request, bpk, rpk):

    pass

    return redirect("board:detail", bpk)

