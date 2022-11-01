# kadaster/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "kadaster"

urlpatterns = [
	path("", views.KadasterIndexView.as_view(), name="kadaster-index"),
]