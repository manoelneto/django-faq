from django.contrib import admin
from models import Question, Topic


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_on',
                    'updated_on', 'status']
    list_editable = ['status']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic)
