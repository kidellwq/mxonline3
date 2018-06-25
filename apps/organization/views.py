from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserForm


# 机构列表
class OrgView(View):
    def get(self, request):
        # 取出所有机构数据
        all_orgs = CourseOrg.objects.all()
        # 取出所有城市数据
        all_citys = CityDict.objects.all()

        #筛选出城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            # 我们就在机构中作进一步筛选类别
            all_orgs = all_orgs.filter(category=category)

        # 计算出有多少机构
        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 4, request=request)
        orgs = p.page(page)
        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')

        return render(request, 'org-list.html', {
            'all_orgs': all_orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'orgs': orgs,
        })


# 我要学习
class AddUserAskView(View):
    def post(self, request):
        userask_form = UserForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status': 'fail', 'msg':{0}}".format(userask_form.errors), content_type='application/json')