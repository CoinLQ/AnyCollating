import math
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from core.catalogue.models import LQSutra

from .serializers import SutraSerializer

from rest_framework.decorators import list_route
class SutraViewSet(ModelViewSet):
    serializer_class = SutraSerializer
    queryset = LQSutra.objects.all()

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
