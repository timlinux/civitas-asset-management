# coding=utf-8
"""Project level url handler."""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from core.views.template import MapView

admin.autodiscover()

urlpatterns = [
    url(r'^$', MapView.as_view(), name='map'),
    url(r'^admin/', admin.site.urls),
    url(r'^amlit/', include('amlit.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
