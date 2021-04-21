from django.shortcuts import render
from django.views.generic.base import TemplateView

#def home(request):
#    return render(request, "core/home.html")
#def sample(request):
    #return render(request, "core/sample.html")

class HomePageView(TemplateView):
    template_name = "core/home.html"
    def get(self, request):
        return render(request, self.template_name, {'titulo': 'Mi Web Playground'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"

