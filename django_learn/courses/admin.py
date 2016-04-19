from django.contrib import admin

from .models import Course, step

class StepInline(admin.StackedInline):
    model = step


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline, ]


admin.site.register(Course, CourseAdmin)
admin.site.register(step)

