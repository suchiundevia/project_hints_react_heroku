from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import Course, Category, Chapter, Lecture, Enrollment
from account_app.models import Learner
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CourseListView(ListView):
    model = Course
    template_name = 'course_app/course_home.html'
    context_object_name = 'courses'
    ordering = ['-course_post_date']
    paginate_by = 2


class UserCourseListView(ListView):
    model = Course
    template_name = 'course_app/user_course.html'
    context_object_name = 'courses'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Course.objects.filter(course_author=user).order_by('-course_post_date')


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_app/course_detail.html'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'course_app/course_form.html'
    success_url = '/'
    fields = ['course_title', 'course_subject', 'course_description', 'course_price', 'course_post_date', 'categories']

    def form_valid(self, form):
        form.instance.course_author = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    template_name = 'course_app/course_form.html'
    fields = ['course_title', 'course_subject', 'course_description', 'course_price', 'course_post_date', 'categories']

    def form_valid(self, form):
        form.instance.course_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.course_author:
            return True
        else:
            return False


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/'
    template_name = 'course_app/course_delete.html'

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.course_author:
            return True
        else:
            return False


def create_chapter(request, pk):
    course = Course.objects.get(id=pk)
    chapter_formset = inlineformset_factory(Course, Chapter, fields=(
        'chapter_title', 'chapter_description', 'chapter_resource_link', 'chapter_sequence'), can_delete=False, extra=1)
    if request.method == "POST":
        formset = chapter_formset(request.POST, instance=course)
        if formset.is_valid():
            formset.save()
            return redirect('/', course_id=course.id)
    formset = chapter_formset(instance=course)
    return render(request, 'course_app/chapter_form.html', {'formset': formset})


class ChapterListView(ListView):
    model = Chapter
    template_name = 'course_app/chapter_detail.html'
    context_object_name = 'chapters'
    paginate_by = 2

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs.get('pk'))
        return Chapter.objects.filter(course=course)


def create_lecture(request, pk):
    chapter = Chapter.objects.get(id=pk)
    lecture_formset = inlineformset_factory(Chapter, Lecture, fields=(
        'lecture_title', 'lecture_description', 'lecture_video', 'lecture_sequence'), can_delete=False, extra=1)
    if request.method == "POST":
        formset = lecture_formset(request.POST, instance=chapter)
        if formset.is_valid():
            formset.save()
            return redirect('/', chapter_id=chapter.id)
    formset = lecture_formset(instance=chapter)
    return render(request, 'course_app/lecture_form.html', {'formset': formset})


class LectureListView(ListView):
    model = Chapter
    template_name = 'course_app/lecture_detail.html'
    context_object_name = 'lectures'
    paginate_by = 2

    def get_queryset(self):
        chapter = get_object_or_404(Chapter, id=self.kwargs.get('pk'))
        return Lecture.objects.filter(chapter=chapter)


class ManageCoursesListView(ListView):
    model = Course
    template_name = 'course_app/manage_courses.html'
    context_object_name = 'courses'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Course.objects.filter(course_author=user)


class ManageChaptersListView(ListView):
    model = Chapter
    template_name = 'course_app/manage_chapters.html'
    context_object_name = 'chapters'
    paginate_by = 2

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs.get('pk'))
        return Chapter.objects.filter(course=course)


class ManageLecturesListView(ListView):
    model = Chapter
    template_name = 'course_app/manage_lectures.html'
    context_object_name = 'lectures'
    paginate_by = 2

    def get_queryset(self):
        chapter = get_object_or_404(Chapter, id=self.kwargs.get('pk'))
        return Lecture.objects.filter(chapter=chapter)


class ChapterDeleteView(DeleteView):
    model = Chapter
    success_url = '/'
    template_name = 'course_app/chapter_delete.html'


class LectureDeleteView(DeleteView):
    model = Lecture
    success_url = '/'
    template_name = 'course_app/lecture_delete.html'


def enroll_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    learner = get_object_or_404(Learner, user=request.user)
    enrollment = Enrollment(course=course, learner=learner)
    enrollment.save()

    return render(request, 'course_app/enroll_course.html')


def people_enrolled(request, pk):
    enrollments = Enrollment.objects.filter(course_id=pk)
    count = enrollments.count()
    context = {'count': count}
    return render(request, 'course_app/people_enrolled.html', context)
