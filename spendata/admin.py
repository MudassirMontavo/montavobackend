from django.db.models import get_models, get_app
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# from http://djangosnippets.org/snippets/2066/
app_models = get_app('spendata')
for model in get_models(app_models):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
