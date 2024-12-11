from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from googletrans import Translator

class Home(View):
    def get(self, request):
        return render(request, "main/main.html")
    
    def post(self, request):
        text = request.POST.get("translate")
        language = request.POST.get("language")
        
        if not text or not language:
            error_message = "Please enter text and language!"
            return render(request, "main/result.html", {"error": error_message})

        try:
            translator = Translator()
            translation = translator.translate(text, src="en", dest=language).text
        except Exception as e:
            return HttpResponse(f"error:{e}")

        return render(request, "main/result.html", {"translation": translation})
