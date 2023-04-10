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
