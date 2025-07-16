from django.urls import path
# Import views
from .views import ExcelAgentView

urlpatterns = [
    path('process/', ExcelAgentView.as_view(), name='Process excel'),
]