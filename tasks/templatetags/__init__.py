from django import template
from datetime import date

register = template.Library()


@register.filter
def days_left(deadline):
    if not deadline:
        return ""

    today = date.today()
    diff = (deadline - today).days

    if diff < 0:
        return "Expired"

    return f"{diff} days left"