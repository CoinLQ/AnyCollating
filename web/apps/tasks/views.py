# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView, TemplateView, DetailView
from core.catalogue.models import Sutra, Reel, LQSutra
from .models import Task
from django.shortcuts import render, get_object_or_404

from django.views.generic.base import RedirectView
from annoying.functions import get_object_or_None
from annoying.decorators import render_to
from annoying.decorators import ajax_request

class VerifySutraView(DetailView):
    model = LQSutra
    template_name = "verify_sutra.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VerifySutraView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        sutras = self.get_object().sutras.all()
        sutras_list = []
        for sutra in sutras:
            sutras_list.append({ 'name': sutra.display, 'reel_list': sutra.reels.all() })
        context['sutra_list'] = sutras_list
        context['task_reels'] = Task.objects.filter(creator=self.request.user, task_type=0).values_list('object_id', flat=True).distinct()
        return context

@render_to()
def start(request):
    task = get_object_or_None(Task, id=request.user.staff_of.prefer_task_id)
    if (task.task_type == 0):
        template_name = 'verify_task.html'
    else:
        template_name = 'collating_task.html'

    return {'task': {'id': task.id, 'task_type': task.task_type, 'percent': task.percent, 'status': task.status},'TEMPLATE': template_name}

@ajax_request
def verify_sutra_choice(request, pk):
    reel = Reel.objects.get(pk=pk)
    task = Task(creator=request.user, content_object=reel, name=u'校对'+reel.__unicode__())
    task.save()
    request.user.staff_of.prefer_task_id = task_id
    request.user.staff_of.save()
    task.build_pages()
    return {'status': 0}

@render_to()
def select(request, task_id):

    task = get_object_or_None(Task, id=task_id)
    if (task.task_type == 0):
        template_name = 'verify_task.html'
    else:
        template_name = 'collating_task.html'
    request.user.staff_of.prefer_task_id = task_id
    request.user.staff_of.save()
    return {'task': {'id': task.id, 'task_type': task.task_type, 'percent': task.percent, 'status': task.status}, 'TEMPLATE': template_name}
