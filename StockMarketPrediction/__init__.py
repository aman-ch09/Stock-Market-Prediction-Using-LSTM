from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so tasks can be registered properly.
from .celery import app as celery_app

__all__ = ['celery_app']
