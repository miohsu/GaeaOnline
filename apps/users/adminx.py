import xadmin
from users.models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_field = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
