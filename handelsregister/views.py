# handelsregister/views.py

# django
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
  
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"]    = 'handelsregister-index'
		return context
