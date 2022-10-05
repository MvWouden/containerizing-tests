from uuid import uuid4

from django.db import models


class ToDo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=256, blank=False, unique=True)
    content = models.TextField(max_length=1024, blank=True, default='')
    completed = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        get_latest_by = ['-updated_at', '-created_at', 'completed', 'title']
        ordering = ['-updated_at', '-created_at', 'completed', 'title']
        verbose_name = 'ToDo Item'
