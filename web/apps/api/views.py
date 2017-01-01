import math
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from core.catalogue.models import LQSutra, Sutra, Reel
from core.messageset.models import Task, TaskPage

from .serializers import SutraSerializer, TaskSerializer

from rest_framework.decorators import list_route, detail_route


class SutraViewSet(ModelViewSet):
    serializer_class = SutraSerializer
    queryset = Sutra.objects.all()

    @list_route(methods=['get'], url_path='treemap')
    def treemap(self, request):
        sutras = LQSutra.objects.filter(is_opened=True)
        ret = []
        for sutra in sutras:
            ret.append({
                'value': int(math.sqrt(sutra.reels_count)),
                'sutra_id': sutra.id,
                'reel': sutra.reels_count,
                'name': sutra.name + '-' + sutra.translator,
                'path': sutra.code
                })

        return Response(ret)

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @detail_route(methods=['get'], url_path='collating')
    def collating(self, request, pk):
        task = Task.objects.get(pk=pk)
        lq_strua = task.content_object
        index = task.pos + 1
        ret = {'current': index, 'name': lq_strua.name, 'total': lq_strua.reels_count, 'variants': []}
        for sutra in lq_strua.sutras.all():
            ret['variants'].append( { 'tripitaka_name': sutra.tripitaka.display,
                    'reels_count': sutra.reels_count,
                    'sutra_code': sutra.code,
                    'reel': Sutra.retrieve_reel_by_index(sutra.code, index),
                })
        return Response(ret)

    @detail_route(methods=['post'], url_path='verify_save')
    def verify_save(self, request, pk):
        task_page = TaskPage.objects.get(pk=pk)
        task_page.text_content_trad = request.data['text_content_trad']
        task_page.save()
        return Response({'id': task_page.id})

    @detail_route(methods=['post'], url_path='verify_shan')
    def verify_shan(self, request, pk):
        task_page = TaskPage.objects.get(pk=pk)
        task_page.status = 1
        task_page.text_content_trad = request.data['text_content_trad']
        task_page.save()
        task_page.task.update_percent()
        return Response({'id': task_page.id})

    @detail_route(methods=['get'], url_path='page_diff_versions')
    def page_diff_versions(self, request, pk):
        task_page = TaskPage.objects.get(pk=pk)
        task_pages = TaskPage.objects.filter(page_id=task_page.page_id, status=1).exclude(pk=task_page.id)
        ret = []
        for item in task_pages:
            ret.append( { 'user': item.task.creator.username,
                    'text_content_trad': item.text_content_trad,
                    'id': 'page-task-' + str(item.id)
                })
        return Response(ret)
