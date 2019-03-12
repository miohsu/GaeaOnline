from organization.models import City, Category, School, Teacher

import xadmin


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_filed = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CategoryAdmin(object):
    list_display = ['name', ]
    search_filed = ['name', ]
    list_filter = ['name', ]


class SchoolAdmin(object):
    list_display = ['name', 'desc', 'category', 'address', 'city', 'click_nums', 'fav_nums', 'image', 'tag', 'add_time']
    search_filed = ['name', 'desc', 'category__name', 'address', 'city__name', 'click_nums', 'fav_nums', 'image', 'tag']
    list_filter = ['name', 'desc', 'category', 'address', 'city', 'click_nums', 'fav_nums', 'image', 'tag', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'age', 'school', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                    'fav_nums', 'image', 'add_time']
    search_filed = ['name', 'age', 'school__name', 'work_years', 'work_company', 'work_position', 'points',
                    'click_nums', 'fav_nums', 'image']
    list_filter = ['name', 'age', 'school', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                   'fav_nums', 'image', 'add_time']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(School, SchoolAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
