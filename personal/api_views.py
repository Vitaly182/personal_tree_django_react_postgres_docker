from rest_framework import generics
from .serializers import EmployeeSerializer
from .models import Employee



class EmployeeApi(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()[:1700]