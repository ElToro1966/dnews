from django.views.generic import TempateView

class HomePageView(TemplateView):
    template_name = 'home.html'
