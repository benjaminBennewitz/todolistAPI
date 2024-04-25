from django.http import HttpResponse
from rest_framework import viewsets
from django.core import serializers

from .serializers import TodoSerializer
from .models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    
    def create(self, request):
        todo = Todo.objects.create(title = request.POST.get('title', 'N/A'), description = request.POST.get('description', 'N/A'), user = request.user)
        serialized_obj = serializers.serialize('json', [todo])
        return HttpResponse(serialized_obj, content_type = 'application/json')