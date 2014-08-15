# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import Topic, Question
from .serializers import TopicSerializer, QuestionSerializer


class TopicViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TopicSerializer
    model = Topic


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = QuestionSerializer
    model = Question
