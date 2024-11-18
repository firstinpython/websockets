from django.core.serializers import serialize
from django.shortcuts import render
from users.models import UsersModel
from projects.models import ProjectsModel
from django.contrib.auth.decorators import login_required
from .serializer import UserSerializer, CreateProjectSerializer, ProjectsSerializer, UsersSerializer, \
    UserRegistrSerializer, TaskSerializer,ProfileUserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.models import StatusModel
from tasks.models import PriorityTaskModel
from tasks.models import TaskModel


# Create your views here.
class UserRegistr(CreateAPIView):
    queryset = UsersModel
    serializer_class = UserRegistrSerializer


@login_required()
@api_view(['GET', 'POST'])
def createpost(request):
    if request.method == 'POST':
        return Response('ok')
    else:
        if request.user.is_authenticated:
            if request.user.role.name_role == "РП":
                return Response("ok")
            else:
                return Response('no')
        return Response('ok')


@login_required()
@api_view(['GET', 'POST'])
def userprofile(request) -> Response:
    if request.method == "GET":
        serializer = UserSerializer(request.user)
        return Response(
            serializer.data
        )


@login_required()
@api_view(['GET'])
def list_projects(request, format=None) -> Response:
    projects = ProjectsModel.objects.all()
    serialize = ProjectsSerializer(projects, many=True)

    return Response(
        serialize.data
    )


@login_required()
@api_view(['POST'])
def create_project(request) -> Response:
    serializer = ProjectsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data
        )


@login_required()
@api_view(['GET', 'DELETE'])
def delete_project(request, pk, format=None) -> Response:
    project = ProjectsModel.objects.filter(id=pk)
    if project:
        project[0].delete()

        return Response(
            {"message": f"{project[0].name_project} was delete"}
        )
    else:
        return Response(
            {"error": "it s very bad"}
        )


@login_required()
@api_view(['GET'])
def retrieve_project(request, pk, format=None) -> Response:
    project = ProjectsModel.objects.filter(id=pk)
    if project:
        serializer = ProjectsSerializer(project[0])
        return Response(
            serializer.data
        )
    else:
        return Response(
            {"error": "it s very bad"}
        )


@login_required()
@api_view(['GET'])
def archival_projects(request) -> Response:
    status_projects = StatusModel.objects.get(id=1)
    projects = ProjectsModel.objects.filter(status=status_projects)
    serializer = ProjectsSerializer(projects, many=True)
    return Response(
        serializer.data
    )


@login_required()
@api_view(['GET'])
def active_projects(request) -> Response:
    status_projects = StatusModel.objects.get(id=2)

    projects = ProjectsModel.objects.filter(status=status_projects)
    serializer = ProjectsSerializer(projects, many=True)
    return Response(
        serializer.data
    )


@api_view(['POST'])
def create_user(request) -> Response:
    if request.method == 'POST':
        serializer = UserSerializer(request)
        return Response(
            {"message": "ok"}
        )


@api_view(['POST'])
def create_task(request) -> Response:
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
        else:
            return Response({"message": "error"})


@api_view(['GET'])
def list_tasks(request,project) -> Response:
    if request.method == 'GET':
        user = UsersModel.objects.filter(username = "tr").first()
        projects = ProjectsModel.objects.filter(pk=project).first()
        model = TaskModel.objects.filter(executor = user,project = projects)
        try:
            serializer = TaskSerializer(model, many=True)
            return Response(
                serializer.data
            )
        except:
            return Response({"message":"в serializer ошибка"})

@api_view(['GET'])
def list_task_admin(request,project) -> Response:
    if request.method == 'POST':
        if request.user.is_superuser:
            mass_task_models = []
            user = UsersModel.objects.filter(projects = project)
            projects = ProjectsModel.objects.filter(pk=project).first()
            for i in user:
                model = TaskModel.objects.filter(executor = i,projects = projects)
                mass_task_models.append(model)
            print(mass_task_models)
            return Response({"message":"ok"})
        else:
            return Response({"message":"user is not superuser"})


@api_view(['GET'])
def profile(request):
    if request.method == 'GET':
        user = UsersModel.objects.filter(username = "tr").first()
        serializer = ProfileUserSerializer(user)
        return Response(serializer.data)

# @api_view(['POST'])
# def create_task(request):
#     if request.method == 'POST':
#         serializer = TaskSerializer()
