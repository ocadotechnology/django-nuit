from django.forms import ModelForm, ValidationError, CharField
from .models import Publisher

class PublisherForm(ModelForm):
    name = CharField(help_text='The name of the publisher')
    class Meta:
        model = Publisher
        fields = ('name', 'address', 'city', 'state_province', 'country', 'website',)
    def clean(self):
        raise ValidationError('Something went wrong')
