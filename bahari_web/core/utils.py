from decimal import Decimal

def pretty_number(
    value: float | int | str,
    places: int = 2,
    curr: str = "",
    sep: str = ".",
    dp: str = ",",
    pos: str = "",
    neg: str = "-",
    trailneg: str = "",
) -> str:
    """Prettify the way number is printed. It also strips out unrequired
    decimal places

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    Code taken from http://docs.python.org/library/decimal.html#recipes

    """

    if not value:
        return "0"

    if isinstance(value, float):
        value = str(value)

    try:
        decimal_value = Decimal(value)
    except ValueError:
        return "0"

    if decimal_value == 0:
        return "0"

    q = Decimal(10) ** -places  # 2 places --> '0.01'
    sign, digits_tuple, exp = decimal_value.quantize(q).as_tuple()

    if digits_tuple == (0,):
        digits_tuple = (0, 0)

    # Modified slightly to truncate on integer part if all decimals are 0
    has_decimals = False
    for digit in digits_tuple[-places:]:
        if digit != 0:
            has_decimals = True
            break

    result: list = []
    digits = list(map(str, digits_tuple))
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)

    if has_decimals:
        for _ in range(places):
            build(next() if digits else "0")
        build(dp)
    else:
        for _ in range(places):
            next()

    if not digits:
        build("0")
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)

    return "".join(reversed(result))
