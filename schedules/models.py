from django.db import models
from settings.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=128)
    detail = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        ordering = ('created_at', )
        db_table = 'posts'

    def __str__(self):
        return f"{self.title} {self.start_date}"
