from django.contrib import admin
from .models import Course, Category, Chapter, Lecture, Enrollment, EnrollmentNotification


class ChapterInline(admin.TabularInline):
    model = Chapter


class LectureInline(admin.TabularInline):
    model = Lecture


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_author', 'course_and_post_date')
    search_fields = ['course_author__username', 'course_title', ]
    list_filter = ('course_post_date', 'categories',)
    fieldsets = (
        ('Relationships',
         {
             'fields': ['course_author', 'categories'],
         }),
        ('Course Details',
         {
             'fields': ['course_title', 'course_subject', 'course_description', 'course_price', 'course_post_date'],
         }),
    )
    inlines = [ChapterInline]

    def course_and_post_date(self, obj):
        return "{} - {}".format(obj.course_title, obj.course_post_date)


admin.site.register(Course, CourseAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description')
    search_fields = ['category_name', ]
    list_filter = ('category_name',)
    fields = ('category_name', 'category_description')


admin.site.register(Category, CategoryAdmin)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('course_and_chapter', 'chapter_sequence')
    search_fields = ['course__course_title', 'chapter_title', ]
    list_filter = ('course', 'chapter_sequence',)
    fieldsets = (
        ('Relationships',
         {
             'fields': ['course'],
         }),
        ('Chapter Details',
         {
             'fields': ['chapter_title', 'chapter_description', 'chapter_resource_link', 'chapter_sequence'],
         }),
    )
    inlines = [LectureInline]

    def course_and_chapter(self, obj):
        return "{} - {}".format(obj.course, obj.chapter_title)


admin.site.register(Chapter, ChapterAdmin)


class LectureAdmin(admin.ModelAdmin):
    list_display = ('chapter_and_lecture', 'lecture_sequence')
    search_fields = ['chapter__chapter_title', 'lecture_title', ]
    list_filter = ('chapter', 'lecture_sequence',)
    fieldsets = (
        ('Relationships',
         {
             'fields': ['chapter'],
         }),
        ('Lecture Details',
         {
             'fields': ['lecture_title', 'lecture_description', 'lecture_video', 'lecture_sequence'],
         }),
    )

    def chapter_and_lecture(self, obj):
        return "{} - {}".format(obj.chapter, obj.lecture_title)


admin.site.register(Lecture, LectureAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'learner')
    search_fields = ['course__course_title', ]
    list_filter = ('course', 'learner',)
    fields = ('course', 'learner')


admin.site.register(Enrollment, EnrollmentAdmin)


class EnrollmentNotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'notification_date', 'enrollment')
    search_fields = ['recipient__username', ]
    list_filter = ('recipient', 'enrollment', 'notification_date',)
    fieldsets = (
        ('Relationships',
         {
             'fields': ['recipient', 'enrollment'],
         }),
        ('Notification Details',
         {
             'fields': ['message', 'notification_date'],
         }),
    )


admin.site.register(EnrollmentNotification, EnrollmentNotificationAdmin)
