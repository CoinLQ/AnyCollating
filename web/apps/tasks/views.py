from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView, TemplateView, DetailView
from core.catalogue.models import Sutra

class StartTaskView(TemplateView):
    template_name = "tasks/start_task.html"

    def get_context_data(self, **kwargs):
        context = super(StartTaskView, self).get_context_data(**kwargs)
        sutra_count = Sutra.objects.count()
        context.update({'sutra_count': sutra_count})
        return context


class SelectTaskView(DetailView):
    template_name = "tasks/start_task.html"