# datasets/views.py

from django.shortcuts import render
from django.views import generic
  
# datasets-index view
# classbased view 
class DatasetsIndexView(generic.TemplateView):
	"""
    Datasaets index page.

    **Template:**

    :template:`datasets/datasets_index.html`
    """
	template_name = "datasets/datasets_index.html"
  
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"]    = 'datasets-index'
		return context

