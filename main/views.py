from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from googletrans import Translator

class Home(View):
    def get(self, request):
        return render(request, "main/main.html")
    
    def post(self, request):
        text = request.POST.get("translate")
        language = request.POST.get("language")

        translator = Translator()
        translation = translator.translate(text, src="en", dest=language).text

        return HttpResponse(translation)

