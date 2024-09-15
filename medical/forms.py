from django import forms

from medical.models import Service, Doctor
from users.forms import StyleFormMixin


class ServiceForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class DoctorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
