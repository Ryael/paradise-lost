from django.contrib import admin
from .models import Ruleset, Army, Unit, Specialism, Wargear, Ability, Keyword, WeaponProfile

# Register your models here.
admin.site.register(Ruleset)
admin.site.register(Army)
admin.site.register(Unit)
admin.site.register(Specialism)
admin.site.register(Wargear)
admin.site.register(Ability)
admin.site.register(Keyword)
admin.site.register(WeaponProfile)
