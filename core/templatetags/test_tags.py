from django import template

register = template.Library()

@register.filter
def get_field(form, field_name):
    return form[field_name]

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})