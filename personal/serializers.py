from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    division = serializers.CharField(source='division.name')
    position = serializers.CharField(source='position.name')

    class Meta:
        model = Employee
        fields = ('id', 'division', 'position', 'first_name', 'last_name', 'patronymic', 'parent_id', 'child_id')