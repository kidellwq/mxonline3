from courses.views import CourseListView, DetailListView, CourseInfoView, CommentsView
from django.urls import path, re_path

app_name = 'course'

urlpatterns = [
    path('list/', CourseListView.as_view(), name='list'),
    re_path('detail/(?P<course_id>\d+)/', DetailListView.as_view(), name='detail'),
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='info'),
    re_path('comments/(?P<course_id>\d+)/', CommentsView.as_view(), name='comments'),
]