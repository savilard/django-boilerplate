from split_settings.tools import include

_base_settings = (
    './api.py',
    './auth.py',
    './base.py',
    './boilerplate.py',
    './db.py',
    './environs.py',
    './i18n.py',
    './installed_apps.py',
    './http.py',
    './media.py',
    './middleware.py',
    './static.py',
    './templates.py',
    './timezone.py',
)

include(*_base_settings)
