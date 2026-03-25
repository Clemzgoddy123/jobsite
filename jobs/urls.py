from django.urls import path

from .views import JobListView, JobDetailView, register, landing

app_name = 'jobs'

urlpatterns = [
    path('', landing, name='landing'),
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('register/', register, name='register'),
]
