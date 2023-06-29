from django.forms import ModelForm
from .models import MailAddress

class Mailform(ModelForm):
    class Meta:
        model  = MailAddress
        fields = '__all__'

