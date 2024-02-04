from django import template

register = template.Library()


@register.filter
def in_category(goods, category):
    return goods.filter(type=category)
