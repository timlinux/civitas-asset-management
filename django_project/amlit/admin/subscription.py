__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/03/21'

from django.contrib import admin
from djstripe.admin import ProductAdmin
from djstripe.models import Product
from amlit.models.subscription import AmlitProduct

admin.site.unregister(Product)


class AmlitProductInline(admin.StackedInline):
    model = AmlitProduct
    extra = 0


class AmlitProductAdmin(ProductAdmin):
    list_display = ("name", "type", "active", "url", "statement_descriptor", "max_user")
    inlines = (AmlitProductInline,)

    def max_user(self, obj):
        return obj.amlitproduct.max_user


admin.site.register(Product, AmlitProductAdmin)
