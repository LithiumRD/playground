from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = 'Mi super web Playgroud'
    #     return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Mi super Playground con contexto modificado en get'})


class SamplePageView(TemplateView):
    template_name = "core/Sample.html"

# def home(request):
#     return render(request, "core/home.html")


# def sample(request):
#     return render(request, "core/sample.html")
