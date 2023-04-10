from django.contrib import admin
from .models import Ruleset, Army, Unit, Specialism

# Register your models here.
admin.site.register(Ruleset)
admin.site.register(Army)
admin.site.register(Unit)
admin.site.register(Specialism)
