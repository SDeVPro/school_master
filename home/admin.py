from django.contrib import admin
from home.models import ContactMessage,Post,Teacher,Student, SchoolSetting
# Register your models here.


admin.site.register(ContactMessage)

admin.site.register(Post)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(SchoolSetting)

