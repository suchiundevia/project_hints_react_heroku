from django.apps import AppConfig


class AccountAppConfig(AppConfig):
    name = 'account_app'

    def ready(self):
        import account_app.signals
