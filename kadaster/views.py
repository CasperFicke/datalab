# kadaster/views.py

from django.shortcuts import render
from django.views import generic

# kadaster-index view
# classbased view 
class KadasterIndexView(generic.TemplateView):
	"""
    Website Kadaster index page.

    **Template:**

    :template:`kadaster/kadaster_index.html`
    """
	template_name = "kadaster/kadaster_index.html"


