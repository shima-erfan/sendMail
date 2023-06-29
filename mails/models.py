from django.db import models
import uuid

# Create your models here.
class MailAddress(models.Model):
    name    = models.CharField(max_length=200, null=True, blank=True)
    address = models.EmailField(max_length=200, null=True, blank=True)
    id      = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) :
        return self.name
