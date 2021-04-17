__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '17/04/21'

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from djstripe.models import Product


class AmlitProduct(models.Model):
    """
    Contains extension of product from dj stripe
    """

    # check current active subscription
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product')
    )
    max_user = models.IntegerField(_('Max user'))

    def __str__(self):
        return self.product.name


@receiver(post_save, sender=Product, dispatch_uid="autocreate_amlit_product")
def update_stock(sender, instance, **kwargs):
    AmlitProduct.objects.get_or_create(
        product=instance, defaults={'max_user': 0})
