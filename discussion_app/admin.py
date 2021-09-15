from django.contrib import admin
from .models import Meeting, TimeSlot


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('meeting_time', 'meeting_status', 'learner')
    search_fields = ['meeting_title', 'meeting_status', ]
    list_filter = ('meeting_status', 'time_slot',)
    fieldsets = (
        ('Relationships',
         {
             'fields': ['time_slot', 'learner'],
         }),
        ('Meeting Details',
         {
             'fields': ['meeting_title', 'meeting_status', 'meeting_description', ],
         }),
    )

    def meeting_time(self, obj):
        return "{} - {}".format(obj.meeting_title, obj.time_slot)


admin.site.register(Meeting, MeetingAdmin)


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'date', 'booked')
    search_fields = ['user__username', 'time', 'date', 'booked', ]
    list_filter = ('time', 'date', 'booked',)
    fields = ('user', 'time', 'date', 'booked')


admin.site.register(TimeSlot, TimeSlotAdmin)
