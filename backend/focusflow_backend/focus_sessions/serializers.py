from rest_framework import serializers
from .models import FocusSession

class FocusSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FocusSession
        fields = ['id', 'start_time', 'end_time', 'is_active', 'duration']
        read_only_fields = ['id', 'start_time', 'duration']
