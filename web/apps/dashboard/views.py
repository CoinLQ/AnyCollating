from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView, TemplateView, DetailView
from core.catalogue.models import Sutra

class IndexView(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        sutra_count = Sutra.objects.count()
        context.update({'sutra_count': sutra_count})
        return context
