from django.shortcuts import render
from googletrans import Translator
import googletrans

# Create your views here.
def index(request):

    ot = request.GET.get("text", "")
    sl = request.GET.get("sl", "ko")
    dl = request.GET.get("dl", "en")

    if ot != "":
        tl = Translator().translate(ot, src=sl, dest=dl).text
    else:
        tl = ""

    context = {
        "text": ot,
        "sl" : sl,
        "dl" : dl,
        "tl" : tl,
        "lang" : googletrans.LANGUAGES,
    }

    return render(request, "trans/index.html", context)