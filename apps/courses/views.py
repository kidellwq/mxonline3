from django.shortcuts import render
from django.views.generic.base import View
from courses.models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# 列表页
class CourseListView(View):
    def get(self, request):
        all_course = Course.objects.all()
        hot_courses = Course.objects.all().order_by("-students")[:3]

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_course = all_course.order_by('-students')
            elif sort == 'hot':
                all_course = all_course.order_by('-click_nums')

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 4, request=request)
        orgs = p.page(page)

        return render(request, 'course-list.html', {
            'all_course': orgs,
            'sort': sort,
            'hot_courses': hot_courses,
        })


# 详情页
class DetailListView(View):
    def get(self, request):
        return render(request, 'course-detail.html', {})
