from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Test(LoginRequiredMixin, TemplateView):
    template_name = 'test.html'


class Thanks(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'