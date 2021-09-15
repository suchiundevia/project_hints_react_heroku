from django.apps import AppConfig


class DiscussionAppConfig(AppConfig):
    name = 'discussion_app'

    def ready(self):
        import discussion_app.signals
