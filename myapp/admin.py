from django.contrib import admin
from .models import Student, Photo


admin.site.register(Photo)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','level','registered_courses')

    def level(self, obj):
        levels = Order.objects.filter(student=obj)
        count = 0
        list_of_levels = ''
        for level in levels:
            list_of_levels += str(level.levels)
            count += 1
            if count < len(levels):
                list_of_levels += ", "
        return list_of_levels

    def registered_courses(self, obj):
        courses = Order.objects.filter(student=obj)
        list_of_course = ""
        count = 0
        for course in courses:
            list_of_course += course.course.name
            count +=1
            if count < len(courses):
                list_of_course += ", "
        return list_of_course


admin.site.register(Student, StudentAdmin)