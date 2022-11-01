# handelsregister/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "handelsregister"

urlpatterns = [
	path('handelsregister/', views.HandelsregisterIndexView.as_view(), name="handelsregister-index"),
]