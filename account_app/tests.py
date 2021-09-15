from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from .models import UserProfile
from django.contrib.auth.models import User
from .views import signup, profile, UserDeleteView
from .forms import UserSignUpForm, UserUpdateForm, UserProfileUpdateForm


class TestViews(TestCase):
    fixtures = ["user_data.json"]

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.profile_url = reverse('profile')
        self.username = 'testuser'
        self.password = 'testing321'
        self.email = 'suchi.undevia@gmail.com'
        self.first_name = 'test'
        self.last_name = 'user'

    def test_signup_POST_method_with_data(self):
        response = self.client.post(self.signup_url, data={
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
        })
        self.assertEquals(response.status_code, 302)
        users = User.objects.all()
        self.assertEqual(users.count(), 22)

    def test_signup_POST_method_no_data(self):
        response = self.client.post(self.signup_url)
        self.assertEquals(response.status_code, 200)
        users = User.objects.all()
        self.assertEqual(users.count(), 21)

    def test_profile_redirect(self):
        data = User.objects.get(pk=2)
        self.client.login(username=data.username, password=data.password)
        response = self.client.post(reverse('profile'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_app/login.html')


class TestForms(TestCase):
    fixtures = ['user_data.json', 'user_profile_data.json']

    def test_user_signup_form_valid_data(self):
        form = UserSignUpForm(data={
            'username': 'testuser',
            'password1': 'testing321',
            'password2': 'testing321',
            'email': 'suchi.undevia@gmail.com',
            'first_name': 'test',
            'last_name': 'user',
        })
        self.assertTrue(form.is_valid())

    def test_user_signup_form_no_data(self):
        form = UserSignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_user_update_form_valid_data(self):
        data = User.objects.get(pk=2)
        form = UserUpdateForm(data={
            'username': data.username,
            'email': data.email,
            'first_name': data.first_name,
            'last_name': data.last_name,
        })
        self.assertFalse(form.is_valid())

    def test_user_update_form_no_data(self):
        form = UserUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_user_profile_update_form_valid_data(self):
        data = UserProfile.objects.get(pk=2)
        form = UserUpdateForm(data={
            'about': data.about,
            'qualification': data.qualification,
            'experience': data.experience,
        })
        self.assertFalse(form.is_valid())

    def test_user_profile_update_form_no_data(self):
        form = UserProfileUpdateForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)


class TestUrls(SimpleTestCase):

    def test_profile_view_url(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_signup_view_url(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signup)

    def test_login_view_url(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_view_url(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_password_reset_view_url(self):
        url = reverse('password_reset')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetView)

    def test_password_reset_done_view_url(self):
        url = reverse('password_reset_done')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

    def test_password_reset_complete_view_url(self):
        url = reverse('password_reset_complete')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)

    def test_user_delete_view_url(self):
        url = reverse('user-delete', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserDeleteView)
