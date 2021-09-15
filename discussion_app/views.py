from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Meeting, TimeSlot
from account_app.models import Learner
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class MeetingCreateView(LoginRequiredMixin, CreateView):
    model = Meeting
    template_name = 'discussion_app/meeting_form.html'
    success_url = '/'
    fields = ['meeting_title', 'meeting_status', 'meeting_description', ]

    def form_valid(self, form):
        user = get_object_or_404(User, username=self.request.user)
        form.instance.learner = get_object_or_404(Learner, user=user)
        form.instance.time_slot = get_object_or_404(TimeSlot, id=self.kwargs.get('pk'))
        return super().form_valid(form)


class MeetingListView(ListView):
    model = Meeting
    template_name = 'discussion_app/meeting_detail.html'
    context_object_name = 'meetings'

    def get_queryset(self):
        learner = get_object_or_404(Learner, id=self.kwargs.get('pk'))
        return Meeting.objects.filter(learner=learner)


class TimeSlotCreateView(LoginRequiredMixin, CreateView):
    model = TimeSlot
    template_name = 'discussion_app/timeslot_form.html'
    success_url = '/'
    fields = ['time', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AllTimeSlotListView(ListView):
    model = TimeSlot
    template_name = 'discussion_app/timeslots.html'
    context_object_name = 'timeslots'
    ordering = ['time', 'date']
    paginate_by = 2

    def get_queryset(self):
        return TimeSlot.objects.exclude(booked=True)


class TimeSlotListView(ListView):
    model = TimeSlot
    template_name = 'discussion_app/timeslot_detail.html'
    context_object_name = 'timeslots'
    ordering = ['time', 'date']
    paginate_by = 2

    def get_queryset(self):
        user = User.objects.filter(username=self.kwargs.get('username')).values('id')[0].get('id')
        return TimeSlot.objects.filter(user=user)


class TimeSlotDeleteView(DeleteView):
    model = TimeSlot
    success_url = '/'
    template_name = 'discussion_app/timeslot_delete.html'
