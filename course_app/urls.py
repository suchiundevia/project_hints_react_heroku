from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, \
    UserCourseListView, ChapterListView, LectureListView, ManageCoursesListView, ManageChaptersListView, \
    ManageLecturesListView, ChapterDeleteView, LectureDeleteView

from . import views

urlpatterns = [
    # List all courses
    path('all/', CourseListView.as_view(), name='course-home'),
    # Activities listed per selected user
    path('user/<str:username>', UserCourseListView.as_view(), name='user-course'),
    # Detail view of an activity (by primary key or link from the title of list view)
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    # Add an activity
    path('new/', CourseCreateView.as_view(), name='course-create'),
    # Update an activity
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    # Delete an activity
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    # Add chapter
    path('newChapter/<int:pk>/', views.create_chapter, name='chapter-create'),
    # Chapters per selected course
    path('<int:pk>/chapters', ChapterListView.as_view(), name='chapter-detail'),
    # Lectures per selected chapter
    path('<int:pk>/lecture', LectureListView.as_view(), name='lecture-detail'),
    # Add lecture
    path('newLecture/<int:pk>/', views.create_lecture, name='lecture-create'),
    # Manage courses
    path('<str:username>/manageCourses/', ManageCoursesListView.as_view(), name='manage-courses'),
    # Manage chapters
    path('<int:pk>/manageChapters/', ManageChaptersListView.as_view(), name='manage-chapters'),
    # Manage lectures
    path('<int:pk>/manageLectures/', ManageLecturesListView.as_view(), name='manage-lectures'),
    # Delete an chapter
    path('<int:pk>/deleteChapter/', ChapterDeleteView.as_view(), name='chapter-delete'),
    # Delete an lecture
    path('<int:pk>/deleteLecture/', LectureDeleteView.as_view(), name='lecture-delete'),
    # Enroll
    path('<int:pk>/enroll/', views.enroll_course, name='enroll'),
    # People enrolled
    path('<int:pk>/membersEnrolled/', views.people_enrolled, name='people-enrolled'),
]
