from organization.views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView, TeacherListView
from django.urls import path, re_path

app_name = 'org'
urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    path('add_fav/', AddFavView.as_view(), name='add_fav'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list'),
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name='org_home'),
    re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name='org_course'),
    re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name='org_desc'),
    re_path('teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name='org_teacher'),

]
