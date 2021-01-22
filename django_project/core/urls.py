# coding=utf-8
"""Project level url handler."""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from core.views.user import UserDetailView

admin.autodiscover()

USER_URL = [
    url(r'^(?P<username>[\w\+%_& ]+)', UserDetailView.as_view(), name='user-detail'),
]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^user/', include(USER_URL)),
    url(r'^', include('amlit.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
