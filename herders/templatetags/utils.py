from django import template

register = template.Library()


@register.filter
def get_range(value):
    if value is not None:
        return range(value)
    else:
        return 0


@register.filter
def absolute(value):
    return abs(value)


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def remove_extension(string):
    return string.replace('.png', '').replace("'", "").replace('(', '_').replace(')', '_')


# Get dictionary key by string
@register.filter
def key(d, key_name):
    return d[key_name]


@register.filter
def humanize_number(value):
    powers = [10 ** x for x in (3, 6, 9, 12)]
    human_powers = ('K', 'M', 'B', 'T')
    try:
        index, hp = next((i, p) for i, p in enumerate(human_powers)
                         if 10 ** 3 > value / powers[i] > 0)
        return_value = "%.{fraction_point}f".format(
            fraction_point=1) % (float(value) / powers[index])
        return_value = return_value \
            if float(return_value) != int(float(return_value)) \
            else str(int(float(return_value)))
        return "%s%s" % (return_value, hp)
    except (IndexError, StopIteration):
        return value


@register.filter
def timedelta(delta):
    if delta:
        total_seconds = delta.total_seconds()
        minutes = int(total_seconds // 60)
        seconds = total_seconds - minutes * 60
        return f'{minutes:02d}:{seconds:2.3f}'
    else:
        return ''
