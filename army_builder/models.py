from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    Automatically adds timestamps and name fields to inherited models.
    """
    class Meta:
        abstract = True

    name = models.CharField(null=False, blank=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Ruleset(BaseModel):
    """
    Stores ruleset data.
    """

class Army(BaseModel):
    """
    Stores army data.
    """
    class Meta:
        verbose_name_plural = "Armies"

    ruleset = models.ForeignKey(Ruleset, on_delete=models.CASCADE, null=False, blank=False)

class Ability(BaseModel):
    """
    Stores ability rules.
    """
    class Meta:
        verbose_name_plural = "Abilities"

    rule = models.TextField()

class Specialism(BaseModel):
    """
    Stores specialism information.
    """
    abilities = models.ManyToManyField(Ability)

class WeaponProfile(BaseModel):
    """
    Stores weapon statistics.
    """
    range = models.CharField(max_length=4)
    type = models.CharField(max_length=50)
    strength = models.CharField(max_length=3)
    armor_penetration = models.CharField(max_length=3)
    damage = models.CharField(max_length=5)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE, null=True, blank=True)


class Wargear(BaseModel):
    """
    Stores wargear statistics.
    """
    class Meta:
        verbose_name_plural = "Wargear"

    points_cost = models.SmallIntegerField(default=0, null=False, blank=False)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE, null=True, blank=True)
    weapon_profiles = models.ManyToManyField(WeaponProfile, blank=True)

class Option(BaseModel):
    """
    Stores options for user selection.
    """
    no_to_select = models.SmallIntegerField(default=-1, null=False, blank=False)
    abilities = models.ManyToManyField(Ability, blank=True)
    wargear = models.ManyToManyField(Wargear, blank=True)
    nested_options = models.ManyToManyField("self", blank=True)

class Keyword(BaseModel):
    """
    Stores unit keywords.
    """

class Unit(BaseModel):
    """
    Stores unit's unique characteristics.
    """
    army = models.ForeignKey(Army, on_delete=models.CASCADE, null=False, blank=False)
    move = models.CharField(max_length=3)
    weapon_skill = models.CharField(max_length=3)
    ballistics_skill = models.CharField(max_length=3)
    strength = models.CharField(max_length=3)
    toughness = models.CharField(max_length=3)
    wounds = models.CharField(max_length=3)
    attacks = models.CharField(max_length=3)
    leadership = models.CharField(max_length=3)
    armour_save = models.CharField(max_length=3)
    max_units = models.CharField(max_length=3)
    points_cost = models.SmallIntegerField(default=0, null=False, blank=False)
    specialisms = models.ManyToManyField(Specialism)
    wargear = models.ManyToManyField(Wargear)
    abilities = models.ManyToManyField(Ability)
    keywords = models.ManyToManyField(Keyword)
