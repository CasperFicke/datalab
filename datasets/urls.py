# datasets/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "datasets"

urlpatterns = [
	path('datasets/', views.DatasetsIndexView.as_view(), name="datasets-index"),
]