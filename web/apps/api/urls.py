from rest_framework import routers
from .views import SutraViewSet
from django.conf.urls import include, url, patterns

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'sutra', SutraViewSet)


urlpatterns = patterns(
  '',
  url(r'^', include(router.urls)),
)