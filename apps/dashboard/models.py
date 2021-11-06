from django.db import models
from django.utils import timezone


class TodoManager(models.Manager):
    def to_list(self):
        todos = self.get_queryset()
        return [todo.to_json() for todo in todos]


class Todo(models.Model):
    STATUS_CHOICES = [
        ("done", "done"),
        ("outstanding", "outstanding"),
    ]
    detail = models.CharField(max_length=500)
    created = models.DateField(default=timezone.now, null=False)
    status = models.CharField(
        max_length=100, null=True, blank=True, choices=STATUS_CHOICES
    )
    updated = models.DateField(default=timezone.now, null=False)

    objects = TodoManager()

    def to_json(self):

        return {
            "created": self.created.strftime("%Y-%m-%d"),
            "detail": self.detail,
            "status": self.status,
        }
