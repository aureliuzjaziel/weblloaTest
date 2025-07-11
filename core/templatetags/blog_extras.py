from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Template filter para obtener un item de un diccionario por su key
    Uso: {{ my_dict|get_item:my_key }}
    """
    return dictionary.get(key, [])
