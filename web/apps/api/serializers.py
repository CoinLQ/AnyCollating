from rest_framework.serializers import ModelSerializer

from core.catalogue.models import Sutra, Page, Reel
from core.messageset.models import Task, TaskPage


class SutraSerializer(ModelSerializer):
    class Meta:
        model = Sutra


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'code', 'page_num', 'image_url', 'text_content_trad')

class ReelSerializer(ModelSerializer):
    class Meta:
        model = Reel
        depth = 2

class TaskPageSerializer(ModelSerializer):
    page = PageSerializer(many=False)
    class Meta:
        model = TaskPage
        fields = ('id', 'page', 'status', 'text_content_trad')
        depth = 2

class TaskSerializer(ModelSerializer):
    task_pages = TaskPageSerializer(many=True)
    reel = ReelSerializer(many=False)
    class Meta:
        model = Task
        fields = ('id', 'task_type', 'percent', 'pos', 'status', 'start_time', 'end_time', 'task_pages', 'reel')
        depth = 2