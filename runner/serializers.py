from rest_framework import serializers

from runner.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
