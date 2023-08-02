from django.apps import AppConfig

class CardConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    default_app_config = 'card.apps.CardConfig'
    name = 'card'

    def ready(self):
        # Importing the model class here will trigger the model registration in the admin site
        from .models import Subject_mark
