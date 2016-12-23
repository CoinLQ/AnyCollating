from rest_framework.serializers import ModelSerializer

from core.catalogue.models import Sutra

class SutraSerializer(ModelSerializer):
    class Meta:
        model = Sutra
        fields = ('id', 'code')
