# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Topic, Question


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
