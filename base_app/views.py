from django.shortcuts import render
from course_app.models import Course, Lecture, Category


def home(request):
    lectures = Lecture.objects.all().select_related().select_related()
    courses = Course.objects.all()
    # categories_with_courses = Category.objects.all().exclude(
    #     id__in=(Category.objects.all().exclude(id__in=(Course.objects.all().values('categories')))))
    return render(request, 'base_app/home.html', {'courses': courses, 'lectures': lectures})


def about(request):
    return render(request, 'base_app/about.html', {'title': 'About'})
