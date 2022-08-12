from django.urls import path

from jobs.api.views import JobDetailAPIView, JobListCreateAPIView

urlpatterns = [
    path('jobs/', view=JobListCreateAPIView.as_view(), name="jobs-list"),
    path('jobs/<int:pk>/', view=JobDetailAPIView.as_view(), name="jobs-detail"),
]