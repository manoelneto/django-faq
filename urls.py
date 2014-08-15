# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from .api_views import (
    TopicViewSet, QuestionViewSet
)
router = DefaultRouter()

router.register(
    r'/topic',
    TopicViewSet,
    'api-topic'
)

router.register(
    r'/question',
    QuestionViewSet,
    'api-question'
)

urlpatterns = router.urls
