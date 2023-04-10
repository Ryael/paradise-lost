from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    Automatically adds timestamps and name fields to inherited models.
    """
    name = models.CharField(null=False, blank=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

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
    ruleset = models.ForeignKey(Ruleset, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Armies"

class Specialism(BaseModel):
    """
    Stores ability information.
    """

class Wargear(BaseModel):
    """
    Stores wargear statistics.
    """
    range = models.CharField(max_length=4)
    type = models.CharField(max_length=50)
    strength = models.CharField(max_length=3)
    armor_penetration = models.CharField(max_length=3)
    damage = models.CharField(max_length=5)
    points_cost = models.SmallIntegerField(default=0, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Wargear"

class Unit(BaseModel):
    """
    Stores unit's unique characteristics.
    """
    army = models.ForeignKey(Army, on_delete=models.CASCADE)
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
    keywords = models.TextField()
    points_cost = models.SmallIntegerField(default=0, null=False, blank=False)
    specialisms = models.ManyToManyField(Specialism)
    wargear = models.ManyToManyField(Wargear)
