from courses.models import Course, Chapter, Category, Video, CourseResource

import xadmin


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'study_time', 'students', 'fav_nums', 'image', 'click_nums',
                    'category', 'tag', 'add_time']
    search_field = ['name', 'desc', 'detail', 'degree', 'study_time', 'students', 'fav_nums', 'image', 'click_nums',
                    'category__name', 'tag']
    list_filter = ['name', 'desc', 'detail', 'degree', 'study_time', 'students', 'fav_nums', 'image', 'click_nums',
                   'category', 'tag', 'add_time']


class ChapterAdmin(object):
    list_display = ['course', 'name', 'study_time', 'add_time']
    list_filter = ['course', 'name', 'study_time', 'add_time']
    search_filed = ['course__name', 'name', 'study_time']


class CategoryAdmin(object):
    list_display = ['name', ]
    list_filter = list_display
    search_field = list_display


class VideoAdmin(object):
    list_display = ['chapter', 'name', 'study_time', 'add_time']
    list_filter = ['chapter', 'name', 'study_time', 'add_time']
    search_field = ['chapter__name', 'name', 'study_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    list_filter = ['course', 'name', 'download', 'add_time']
    search_field = ['course__name', 'name', 'download']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Video, VideoAdmin)
