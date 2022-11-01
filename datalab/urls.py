# datalab/urls.py

# django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('site_basis.urls', namespace="site-basis")),
  path('', include('kadaster.urls', namespace="kadaster")),
]
