from django.shortcuts import render

from .models import Course

def course_list(request):
    rhr = Course.objects.all()
    return render(request, 'courses/course_list.html', {'rhr': rhr})

def course_detail(request, pk):
    rgb = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'rgb': rgb})