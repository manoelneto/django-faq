import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Topic(models.Model):
    """
    Generic Topics for FAQ question grouping
    """
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Question(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    STATUS_CHOICES = (
        (ACTIVE, _('Active')),
        (INACTIVE, _('Inactive')),
    )

    text = models.TextField(
        _('question'), help_text=_('The actual question itself.')
    )
    answer = models.TextField(
        _('answer'), blank=True, help_text=_('The answer text.')
    )
    topic = models.ForeignKey(
        Topic, verbose_name=_('topic'), related_name='questions',
        blank=True, null=True
    )
    status = models.IntegerField(
        _('status'),
        choices=STATUS_CHOICES, default=ACTIVE,
        help_text=_("Only questions with their status set to 'Active' will be "
                    "displayed. ")
    )

    created_on = models.DateTimeField(
        _('created on'), default=datetime.datetime.now)

    updated_on = models.DateTimeField(_('updated on'))

    class Meta:
        verbose_name = _("Frequent asked question")
        verbose_name_plural = _("Frequently asked questions")
        ordering = ['created_on']

    def __unicode__(self):
        return self.text

    def is_header(self):
        return self.status == Question.HEADER

    def is_active(self):
        return self.status == Question.ACTIVE
