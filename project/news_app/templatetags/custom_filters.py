from django import template

register = template.Library()


@register.filter(name='censor')
def currency(value):
    for i in range(len(value.split())):
        if value.split()[i][0].isupper() and isinstance(value,str):
            value = value.replace(value.split()[i], value.split()[i][0] + '*' * (len(value.split()[i]) - 1))
        elif value.split()[i][0] == '«' and isinstance(value,str):
            value = value.replace(value.split()[i], '«' + value.split()[i][1] + '*' * (len(value.split()[i]) - 3) + '»')
    return value