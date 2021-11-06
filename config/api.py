from ninja import NinjaAPI
from apps.dashboard.api import router as dashboard_router

api = NinjaAPI()

api.add_router("/dashboard/", dashboard_router)
