from django.shortcuts import render
from django.views.generic import (TemplateView, FormView)
# Create your views here.

from ctpe_deals_app.models import Deal

class HomepageView(TemplateView):
	template_name = 'main/home.html'
	
	def get_context_data(self, **kwargs):
		context = super(HomepageView, self).get_context_data(**kwargs)
		deals = Deal.objects.all()

		context['deals'] = deals 
		return context

