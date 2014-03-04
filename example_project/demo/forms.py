from django.forms import ModelForm, ValidationError
from .models import Publisher

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'address', 'city', 'state_province', 'country', 'website',)
    def clean(self):
        raise ValidationError('Something went wrong')