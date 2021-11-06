from django.utils import timezone
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update({"chart_data": self.get_chart_data()})
        return context

    def get_chart_data(self):
        """return chart data"""
        return [
            {"value": 335, "name": "Direct"},
            {"value": 310, "name": "Email"},
            {"value": 274, "name": "Union Ads"},
            {"value": 235, "name": "Video Ads"},
            {"value": 400, "name": "Search Engine"},
        ]
