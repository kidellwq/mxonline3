from courses.views import CourseListView, DetailListView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView
from django.urls import path, re_path

app_name = 'course'

urlpatterns = [
    path('list/', CourseListView.as_view(), name='list'),
    path('add_comment/', AddCommentsView.as_view(), name='add_comment'),
    re_path('detail/(?P<course_id>\d+)/', DetailListView.as_view(), name='detail'),
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='info'),
    re_path('comments/(?P<course_id>\d+)/', CommentsView.as_view(), name='comments'),
    re_path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name='video'),
]