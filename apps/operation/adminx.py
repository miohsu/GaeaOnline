from operation.models import UserConsult, UserCourse, UserFavorite, UserMessage, CourseComment

import xadmin


class UserConsultAdmin(object):
    list_display = ['name', 'mobile', 'course', 'add_time']
    search_field = ['name', 'mobile', 'course__name']
    list_filter = ['name', 'mobile', 'course', 'add_time']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comment', 'add_time']
    search_field = ['user__username', 'course__name', 'comment']
    list_filter = ['user', 'course', 'comment', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_field = ['user__username', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_field = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_field = ['user__username', 'course__name']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserConsult, UserConsultAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
