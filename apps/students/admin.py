from django.contrib import admin
from apps.students.models import Group, Student, ContactPerson


admin.site.register(Group)
admin.site.register(Student)
admin.site.register(ContactPerson)
