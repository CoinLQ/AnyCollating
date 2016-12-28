import math
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from core.catalogue.models import LQSutra, Sutra, Reel
from core.messageset.models import Task

from .serializers import SutraSerializer

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
                'reel': sutra.reels_count,
                'name': sutra.name + '-' + sutra.translator,
                'path': sutra.code
                })

        return Response(ret)

class TaskViewSet(ModelViewSet):
    #serializer_class = TaskSerializer
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

    @detail_route(methods=['get'], url_path='verify')
    def verify(self, request, pk):
        task = Task.objects.get(pk=pk)
        reel = task.content_object
        index = task.pos + 1
        ret = {'current': index, 'name': task.__unicode__(), 'total': task.content_object.page_counts(), 'image_url': task.get_current_page_image()}
        return Response(ret)

