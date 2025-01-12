from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.views import IsManager
from .models import Project
from .serializers import ProjectSerializer

@api_view(["GET"])
@permission_classes([IsManager])
def get_all_projects(request):
    tasks = Project.objects.all()
    serializer = ProjectSerializer(tasks, many=True)
    return Response(serializer.data)
    
    
@api_view(["GET"])
@permission_classes([IsManager])
def get_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"message:":"this company does not exist"})
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsManager])
def delete_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist():
        return Response({"message:":"this project does not exist"})
    project.delete()
    return Response({"message:":"project is deleted"})
    




    