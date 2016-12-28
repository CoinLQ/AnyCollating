from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView, TemplateView, DetailView
from core.catalogue.models import Sutra
from core.messageset.models import Task
from django.shortcuts import render, get_object_or_404

from django.views.generic.base import RedirectView
from annoying.functions import get_object_or_None
from annoying.decorators import render_to

# class StartTaskView(TemplateView):
#     template_name = "start_task.html"

#     def get_context_data(self, **kwargs):
#         context = super(StartTaskView, self).get_context_data(**kwargs)
#         task = get_object_or_None(Task, id=self.request.user.staff_of.prefer_task_id)
#         if task:
#             context.update({'task': {'id': task.id, 'task_type': task.task_type,
#                             'percent': task.percent, 'status': task.status}})
#         return context


class SelectTaskView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'start-task'

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if (task.creator.id != self.request.user.id):
            get_object_or_404(Task, pk=-1)
        staff = self.request.user.staff_of
        staff.prefer_task_id = task.id
        staff.save()
        return '/apps/tasks/start'
        #return super(SelectTaskView, self).get_redirect_url(*args, **kwargs)


class StartTaskView(RedirectView):
    template_name = "start_task.html"

    permanent = False
    query_string = True
    #pattern_name = 'start-task'

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_None(Task, id=self.request.user.staff_of.prefer_task_id)
        if (task.task_type == 0):
            return '/apps/tasks/verify'
        else:
            return '/apps/tasks/verify'

@render_to()
def start(request):
    task = get_object_or_None(Task, id=request.user.staff_of.prefer_task_id)
    if (task.task_type == 0):
        template_name = 'verify_task.html'
    else:
        template_name = 'collating_task.html'

    return {'task': {'id': task.id, 'task_type': task.task_type, 'percent': task.percent, 'status': task.status},'TEMPLATE': template_name}
