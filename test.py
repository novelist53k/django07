# pip : pypi.org에서 다른 개발자들이 개발해놓은 코드를 가져다 사용할 수 있도록 만든 프로그램

# import : 다른 파일의 클래스, 함수, 변수를 가져다 사용할 수 있도로고 만든 구문


from googletrans import Translator
from gtts import gTTS
import googletrans

print(f"사용 가능 언어 : {googletrans.LANGUAGES}")

text1 = "Hello welcome to my website!"

translator = Translator()

print(translator.detect(text1))

trans1 = translator.translate(text1, src='en', dest='zh-cn')

print("English to Japanese: ", trans1.text)


tts = gTTS(trans1.text, lang="zh-cn")
tts.save("hello.mp3")



























