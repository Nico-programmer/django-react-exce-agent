from django.urls import path
# Import views
from .views import ProcessExcelView

urlpatterns = [
    path('process/', ProcessExcelView.as_view(), name='Process excel'),
]