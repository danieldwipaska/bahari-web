from django import template

from bahari_web.core.utils import pretty_number as pretty_number_func

register = template.Library()


@register.filter(name="pretty_number")
def groupNumbers(value: int) -> str:
    return pretty_number_func(value, sep=".", dp=",")


@register.filter(name="abbreviate_number")
def abbreviate_number(value: int, num_decimals: int = 2) -> str:
    int_value = int(value)
    formatted_number = f"{{:.{num_decimals}f}}"
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value / 1000.0).rstrip("0.") + " K"
    elif int_value < 1000000000:
        return formatted_number.format(int_value / 1000000.0).rstrip("0.") + " Mio"
    else:
        return formatted_number.format(int_value / 1000000000.0).rstrip("0.") + " Bio"


@register.filter(name="abs")
def absolute(value: int) -> int:
    return abs(value)
