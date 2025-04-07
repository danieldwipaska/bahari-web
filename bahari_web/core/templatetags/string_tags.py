from datetime import datetime
from typing import List

from django import template
from django.utils import timezone

register = template.Library()


@register.filter(name="split")
def split(value: str, key: str = "\n") -> List[str]:
    """
    Splits the input string into a list of substrings based on a specified delimiter.
    """
    return value.split(key)


@register.filter
def format_iso_date(iso_date_str: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_date_str).astimezone(
            timezone.get_current_timezone()
        )
        return dt.strftime("%d %b %Y, %H:%M")
    except Exception as _:
        return iso_date_str
