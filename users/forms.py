from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import BooleanField

from users.models import User, Record


class StyleFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )


class RecordForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Record
        exclude = ('user', 'is_active', 'diagnosis')


class RecordManageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Record
        fields = ('diagnosis',)
