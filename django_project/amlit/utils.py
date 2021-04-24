from django.conf import settings
from djstripe.models import APIKey, Product
from amlit.models.subscription import AmlitProduct


class AmlitStripe(object):
    """ Contains fast access stripe object for amlit """

    def __init__(self):
        if settings.STRIPE_LIVE_MODE:
            self.public_key = settings.STRIPE_LIVE_PUBLIC_KEY
            self.secret_key = settings.STRIPE_LIVE_SECRET_KEY
        else:
            self.public_key = settings.STRIPE_TEST_PUBLIC_KEY
            self.secret_key = settings.STRIPE_TEST_SECRET_KEY

        self.account = APIKey.objects.get(
            secret=self.secret_key).djstripe_owner_account

    def products(self):
        """ Return products
        """
        return Product.objects.filter(
            djstripe_owner_account=self.account).order_by('amlitproduct__max_user')
