from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    title = models.CharField(max_length=32)
    member = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class Task(models.Model):

    TODO = 'T'
    DONE = 'D'
    STATUS = (
        (TODO, 'TODO'),
        (DONE, 'DONE'),
    )

    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    due_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS, default=TODO, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        #if self.project not in self.owner.project_set.all():
        if not self.owner.project_set.filter(id=self.project.id).exists():
            raise ValidationError({
                'owner': _('Task owner must consist of task related project')
                }, code='required'
            )
