from courses.views import CourseListView, DetailListView
from django.urls import path

app_name = 'course'

urlpatterns = [
    path('list/', CourseListView.as_view(), name='list'),
    path('detail/', DetailListView.as_view(), name='detail'),
]