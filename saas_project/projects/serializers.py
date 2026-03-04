from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ("organization", "created_by")

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["organization"] = request.user.organization
        validated_data["created_by"] = request.user
        return super().create(validated_data)