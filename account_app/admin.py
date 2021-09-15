from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Learner

admin.site.site_header = 'Hints Project Administration'
admin.site.index_title = 'Hints Project Administration'


class UserProfileInline(admin.TabularInline):
    model = UserProfile


class LearnerInline(admin.TabularInline):
    model = Learner


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name')
    search_fields = ['username', 'email', ]
    list_filter = ('is_staff', 'is_superuser', 'date_joined', 'last_login',)
    fieldsets = (
        ('Login Details',
         {
             'fields': ['username', 'password', 'is_superuser', 'is_staff', 'date_joined'],
         }),
        ('User Details',
         {
             'fields': ['first_name', 'last_name', 'email', 'last_login'],
         }),
    )
    inlines = [UserProfileInline, LearnerInline]

    def full_name(self, obj):
        return "{}, {}".format(obj.last_name, obj.first_name)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'about', 'user_qualification')
    search_fields = ['user__username', 'about', ]
    list_filter = ('about', 'image',)
    fields = ('user', 'image', 'about', 'qualification', 'experience')

    def user_qualification(self, obj):
        return "{} - {}".format(obj.user, obj.qualification)


admin.site.register(UserProfile, UserProfileAdmin)


class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['user__username', ]
    list_filter = ('user',)
    fields = ('user',)


admin.site.register(Learner, LearnerAdmin)
