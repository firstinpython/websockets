from django.urls import path
from .views import UserRegistr, createpost, userprofile, list_projects, create_project, retrieve_project, \
    delete_project, archival_projects, active_projects, create_user, create_task, list_tasks, list_task_admin, profile
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("users", UserRegistr.as_view()),
    path("create_user", create_user),
    path("projects", createpost),
    path("archival_projects", archival_projects),
    path("active_projects", active_projects),
    path("profile", userprofile),
    path("create_project", create_project),
    path("list_projects", list_projects),
    path("project/<int:pk>/", retrieve_project),
    path("delete_project/<int:pk>/", delete_project),
    # path("create_task/"),
    path("<int:project>/list_tasks/",list_tasks),
    # path("list_tasks/<int:user_id>/")
    path("<int:project>/list_tasks_admin/",list_task_admin),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("create_task/",create_task),
    path("profile/",profile),


    # path("projects"),
    # path("project/<str:name>/")
]
