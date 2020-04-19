from django.urls import path
from . import views

urlpatterns = [
    path("policies/", views.GetAddPolicies.as_view()),
    path("policies/overview/", views.OverviewPolicy.as_view()),
    path("policies/<pk>/", views.GetUpdateDeletePolicy.as_view()),
    path("<int:pk>/automatedtasks/", views.AutoTask.as_view()),
    path("<int:pk>/policyautomatedtasks/", views.PolicyAutoTask.as_view()),
    path("taskrunner/<int:pk>/", views.TaskRunner.as_view()),
    path("runwintask/<int:pk>/", views.run_task),
]
