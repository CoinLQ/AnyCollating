from rest_framework import routers
from .views import SutraViewSet, TaskViewSet
from django.conf.urls import include, url, patterns

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'sutra', SutraViewSet)
router.register(r'task', TaskViewSet)

urlpatterns = patterns(
  '',
  url(r'^', include(router.urls)),
)