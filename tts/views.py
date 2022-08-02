from django.shortcuts import render
import googletrans
from gtts import gTTS

# Create your views here.
def index(request):

    context = {
        "langs" : googletrans.LANGUAGES,
    }

    if request.method == "POST":
        bf = request.POST.get("bf")
        fn = request.POST.get("fn")
        la = request.POST.get("lang")

        tts = gTTS(bf, lang=la)
        tts.save(f"media/tts/{fn}.mp3")
        
        context.update({
            "b":bf,
            "f":fn,
            "l":la,
        })


    return render(request, "tts/index.html", context)

