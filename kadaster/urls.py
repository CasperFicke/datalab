# kadaster/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "kadaster"

urlpatterns = [
  # Basisregistratie Kadaster
	path('brk/'     , views.KadasterIndexView.as_view(), name="kadaster-index"),
  path('brk/nnp/' , views.brk_nnp, name="brk-nnp"),
  path('brk/np/'  , views.brk_np, name="brk-np"),
  path('brk/zg/'  , views.brk_zg, name="brk-zg"),
  path('brk/oz/'  , views.brk_oz, name="brk-oz"),
]