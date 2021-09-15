from django.urls import path
from .views import MeetingListView, TimeSlotListView, TimeSlotCreateView, AllTimeSlotListView, TimeSlotDeleteView, \
    MeetingCreateView

# Direct views used, refer to the global urls.py file
urlpatterns = [
    # Book meeting
    path('<int:pk>/book/', MeetingCreateView.as_view(), name='book-meeting'),
    # View all meetings
    path('<int:pk>/meetings/', MeetingListView.as_view(), name='all-meetings'),
    # Add time slots
    path('<str:username>/slots/', TimeSlotCreateView.as_view(), name='add-time'),
    # User based time slots
    path('<str:username>/timeslots/', TimeSlotListView.as_view(), name='all-timeslots'),
    # View all time slots
    path('timeslots/', AllTimeSlotListView.as_view(), name='timeslots'),
    # Delete an activity
    path('<int:pk>/delete/', TimeSlotDeleteView.as_view(), name='timeslot-delete'),
]
