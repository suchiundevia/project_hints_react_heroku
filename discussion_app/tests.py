from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import MeetingListView, TimeSlotListView


class TestUrls(SimpleTestCase):

    def test_user_meeting_list_view_url(self):
        url = reverse('all-meetings', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, MeetingListView)

    def test_time_slot_list_view_url(self):
        url = reverse('all-timeslots', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TimeSlotListView)
