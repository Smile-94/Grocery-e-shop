from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # use if you support internationalization

def validate_float_value(value):
    if value < 0.0:
        raise ValidationError(_('Value can not be less than 0.0'), params={'value': value},)

def validate_float_value_with_range(value):
    if value < 0.0 or value > 5.0:
        raise ValidationError(_('The value must be in the range of 0-5'), params={'value': value},)


def min_decimal_value(value):
    if value < 0.0:
        raise ValidationError(_('Value can not be negative number'), params={'value': value},)
