from django.utils import timezone
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    def get_todos(self):
        """Simulate fetch from db"""
        return [
            {
                "date": timezone.now().strftime("%Y-%m-%d"),
                "detail": "example thing",
                "status": "done",
            },
            {
                "date": timezone.now().strftime("%Y-%m-%d"),
                "detail": "example thing",
                "status": "outstanding",
            },
        ]

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update({"todos": self.get_todos})
        return context
