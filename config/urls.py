from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
import os.path

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    # Django i18n (fixes Jazmin 'set_language' error)
    path('i18n/', include('django.conf.urls.i18n')),

    # Django Admin
    path('admin/', admin.site.urls),

    # Wagtail Admin
    path(settings.WAGTAILADMIN_BASE_URL, include(wagtailadmin_urls)),
    # Wagtail Documents
    path('documents/', include(wagtaildocs_urls)),

    # Your app URLs
    path('', include("pages.urls")),
    path('', include("core.urls")),
    path('posts/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    urlpatterns += [
        path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico'))
    ]