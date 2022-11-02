from django.urls import path
from .api_views import EmployeeApi

urlpatterns = [
    path('api/employee/', EmployeeApi.as_view(), name='employee_api'),
]