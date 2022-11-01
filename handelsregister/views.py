# handelsregister/views.py

from django.shortcuts import render
from django.views import generic

# handelsregister-index view
# classbased view 
class HandelsregisterIndexView(generic.TemplateView):
	"""
    Handelsregister index page.

    **Template:**

    :template:`handelsregister/handelsregister_index.html`
    """
	template_name = "handelsregister/handelsregister_index.html"


