# Imports -> Standard
from django.apps import AppConfig


# Config -> Quickstart config to represent the Quickstart app
class QuickstartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quickstart'
