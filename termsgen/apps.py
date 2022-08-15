from django.apps import AppConfig


class TermsgenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'termsgen'

    def ready(self):
        import termsgen.signals
