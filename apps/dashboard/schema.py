from typing import Optional
from django.utils import timezone
from ninja import ModelSchema
from .models import Todo
from datetime import datetime



class TodoSchema(ModelSchema):

    created: Optional[datetime] = timezone.now()
    status: Optional[str] = "outstanding"

    class Config:
        model = Todo
        model_fields = ["id", "detail", "created", "status"]
