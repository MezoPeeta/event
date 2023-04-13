from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'
    label = 'users'

    def ready(self):
        import apps.users.signals

