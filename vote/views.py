from django.shortcuts import redirect, render
from .models import Topic, Choice
from django.utils import timezone

# Create your views here.
def index(request):
    context = {
        "tset" : Topic.objects.all(),
    }
    return render(request, "vote/index.html", context)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    context = {
        "t" : t,
        "cset" : t.choice_set.all(),
    }
    return render(request, "vote/detail.html", context)

def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    
    if not request.user in t.voter.all() :
        cpk = Choice.objects.get(id=request.POST.get("cho"))
        t.voter.add(request.user)
        cpk.choicer.add(request.user)

    return redirect("vote:detail", tpk)

def cancle(request, tpk):
    u = request.user
    t = Topic.objects.get(id=tpk)

    if u in t.voter.all():
        t.voter.remove(u)
        u.choice_set.get(topic=t).choicer.remove(u)


    return redirect("vote:detail", tpk)

def create(request):

    if request.method == "POST":
        rp = request.POST

        t = Topic(subject=rp.get("sub"), maker=request.user, content=rp.get("con"), pubdate=timezone.now())

        cn = rp.getlist("name")
        cp = request.FILES.getlist("pic")
        cc = rp.getlist("ccon")

        t.save()
        for i, j, k in zip(cn, cp, cc):
            c = Choice(topic=t, name=i, pic=j, con=k)
            c.save()

        redirect("vote:index")

    return render(request, "vote/create.html")

def delete(request, tpk):
    t = Topic.objects.get(id=tpk)
    if request.user == t.maker:
        t.delete()
    return redirect("vote:index")