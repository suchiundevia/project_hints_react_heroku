from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, \
    UserCourseListView, ChapterListView, LectureListView, ManageCoursesListView, ManageChaptersListView, \
    ManageLecturesListView, ChapterDeleteView, LectureDeleteView, create_chapter, create_lecture, enroll_course, \
    people_enrolled
from django.test.client import RequestFactory
from .models import Course


class TestViews(TestCase):
    fixtures = ['course_data.json', 'category_data.json', 'chapter_data.json', 'lecture_data.json', 'user_data.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.create_course_url = reverse('course-create')

    def test_create_inventory_view(self):
        user = User.objects.get(pk=3)
        print(user.username + user.password)
        login = self.client.login(username=user.username, password='testing321')
        self.assertTrue(login)
        form = {
            'course_title': 'test course',
            'course_subject': 'test subject',
            'course_description': 'test description',
            'course_price': 0,
            'course_post_date': '2020-09-15T02:58:52Z',
            'course_author': 3,
            'categories': [1, ],
        }
        req_kwargs = {}
        req_kwargs.update({'data': form})
        req = getattr(self.factory, 'post')('course-create', **req_kwargs)
        req.user = user
        response = CourseCreateView.as_view()(req)
        print(req)
        self.assertEqual(Course.objects.all().count(), 7)
        print(Course.objects.all())
        self.assertEquals(response.status_code, 302)

    def test_delete_course_post_request(self):
        data = Course.objects.get(pk=4)
        response = self.client.post(reverse('course-delete', args=[data.pk]))
        self.assertEqual(response.status_code, 302)

    def test_course_list_view(self):
        request = self.factory.get(reverse('course-home'))
        response = CourseListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_user_course_list_view(self):
        username = User.objects.get(pk=8)
        request = RequestFactory().get('user-course')
        view = UserCourseListView.as_view(template_name='user_course.html')
        response = view(request, username=username)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'user_course.html')

    def test_course_detail_view(self):
        course = Course.objects.get(pk=5)
        request = RequestFactory().get('course-detail')
        view = CourseDetailView.as_view(template_name='course_detail.html')
        response = view(request, pk=course.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'course_detail.html')

    def test_chapter_list_view(self):
        course = Course.objects.get(pk=5)
        request = RequestFactory().get('chapter-detail')
        view = ChapterListView.as_view(template_name='chapter_detail.html')
        response = view(request, pk=course.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'chapter_detail.html')


class TestUrls(SimpleTestCase):

    def test_course_list_view_url(self):
        url = reverse('course-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CourseListView)

    def test_user_course_list_view_url(self):
        url = reverse('user-course', args=['such'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserCourseListView)

    def test_course_detail_view_url(self):
        url = reverse('course-detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CourseDetailView)

    def test_course_create_view_url(self):
        url = reverse('course-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CourseCreateView)

    def test_course_update_view_url(self):
        url = reverse('course-update', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CourseUpdateView)

    def test_course_delete_view_url(self):
        url = reverse('course-delete', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CourseDeleteView)

    def test_chapter_create_view_url(self):
        url = reverse('chapter-create', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, create_chapter)

    def test_chapter_list_view_url(self):
        url = reverse('chapter-detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ChapterListView)

    def test_lecture_list_view_url(self):
        url = reverse('lecture-detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LectureListView)

    def test_lecture_create_view_url(self):
        url = reverse('lecture-create', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, create_lecture)

    def test_manage_course_list_view_url(self):
        url = reverse('manage-courses', args=['such'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ManageCoursesListView)

    def test_manage_chapter_list_view_url(self):
        url = reverse('manage-chapters', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ManageChaptersListView)

    def test_manage_lecture_list_view_url(self):
        url = reverse('manage-lectures', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ManageLecturesListView)

    def test_chapter_delete_view_url(self):
        url = reverse('chapter-delete', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ChapterDeleteView)

    def test_lecture_delete_view_url(self):
        url = reverse('lecture-delete', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LectureDeleteView)

    def test_enrolled_course_view_url(self):
        url = reverse('enroll', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, enroll_course)

    def test_people_enrolled_view_url(self):
        url = reverse('people-enrolled', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, people_enrolled)
