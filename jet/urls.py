import django
from django.urls import path

try:
    from django.views.i18n import JavaScriptCatalog
    javascript_catalog = JavaScriptCatalog.as_view()
except ImportError:  # Django < 2.0
    from django.views.i18n import javascript_catalog

from jet.views import add_bookmark_view, remove_bookmark_view, toggle_application_pin_view, model_lookup_view


app_name = 'jet'

urlpatterns = [
    path(
        r'add_bookmark/',
        add_bookmark_view,
        name='add_bookmark'
    ),
    path(
        r'remove_bookmark/',
        remove_bookmark_view,
        name='remove_bookmark'
    ),
    path(
        r'toggle_application_pin/',
        toggle_application_pin_view,
        name='toggle_application_pin'
    ),
    path(
        r'model_lookup/',
        model_lookup_view,
        name='model_lookup'
    ),
    path(
        r'jsi18n/',
        javascript_catalog,
        {'packages': 'django.contrib.admin+jet'},
        name='jsi18n'
    ),
]

if django.VERSION[:2] < (1, 8):
    from django.conf.urls import patterns
    urlpatterns = patterns('', *urlpatterns)
