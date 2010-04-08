import datetime
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.fields import DateField, TimeField, DateTimeField
from parser import parse

class HumanDateTimeField(DateTimeField):
    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return None
        try:
            return parse(value)
        except Exception, e:
            raise ValidationError(self.error_messages['invalid'])

class HumanTimeField(TimeField):
    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return None
        try:
            return parse(value).time()
        except Exception, e:
            raise ValidationError(self.error_messages['invalid'])

class HumanDateField(DateField):
    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return None
        try:
            return parse(value).date()
        except Exception, e:
            raise ValidationError(self.error_messages['invalid'])