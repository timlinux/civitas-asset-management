from django import template

register = template.Library()


@register.simple_tag(name='user_role')
def user_role(organisation, user):
    """ get role of user of organisation """
    return organisation.role(user)


@register.simple_tag(name='is_admin')
def is_admin(organisation, user):
    """ is user admin of organisation """
    return organisation.is_admin(user)
