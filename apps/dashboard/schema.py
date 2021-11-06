from typing import Optional
from django.utils import timezone
from ninja import ModelSchema
from .models import Todo


class TodoSchema(ModelSchema):

    created: Optional = timezone.now()
    status: Optional[str] = "outstanding"

    class Config:
        model = Todo
        model_fields = ["id", "detail", "created", "status"]
