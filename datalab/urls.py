# datalab/urls.py

# django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('site_basis.urls'      , namespace="site-basis")),
  path('', include('kadaster.urls'        , namespace="kadaster")),
  path('', include('handelsregister.urls' , namespace="handelsregister")),
  path('', include('datasets.urls'        , namespace="datasets")),
   # debug urls
  path("__debug__", include('debug_toolbar.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

