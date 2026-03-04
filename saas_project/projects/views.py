from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        return Project.objects.filter(
            organization=self.request.user.organization
        )