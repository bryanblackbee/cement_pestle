from django.shortcuts import render

# Create your views here.
from django.views.generic import (TemplateView, FormView)

from ctpe_deals_app.models import (Category, Deal, Tag)
from ctpe_deals_app.forms import (AddMultipleDealsForm, AddDealsFormset, 
	AddNewDealForm)

from django.urls import reverse

class AddDealsView(FormView):
	template_name = 'deals/add_deals.html'
	form_class = AddMultipleDealsForm

	def get_context_data(self, **kwargs):
		context = super(AddDealsView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['deals'] = AddDealsFormset(self.request.POST)
		else:
			context['deals'] = AddDealsFormset()
		return context

	def get_form(self, form_class=None):
		form = super(AddDealsView, self).get_form(form_class)
		form.fields['category_id'].choices = (Category.objects.
			all().values_list('id', 'category_name'))
		return form

	def form_valid(self, form):
		context = self.get_context_data()
		deals = context['deals']
		if form.is_valid() and deals.is_valid():
			# Get the category
			sel_category_id = int(form.cleaned_data['category_id'])
			category = Category.objects.get(id=sel_category_id)

			for d in deals:
				# Create the deal & save it
				d_name = d.cleaned_data.get('deal_name')
				d_text = d.cleaned_data.get('deal_text')
				dl = Deal(for_category=category, deal_name=d_name, deal_text=d_text)
				dl.save(force_insert=True)

		return super(AddDealsView, self).form_valid(form)

	def get_success_url(self):
		return reverse('home')

class DealCategoryView(TemplateView):
	template_name = 'main/home.html'

	def get_context_data(self, **kwargs):
		context = super(DealCategoryView, self).get_context_data(**kwargs)
		category = self.kwargs['category'].lower()
		deals = Deal.objects.filter(for_category__category_name=category)
		context['deals'] = deals
		return context

class AddNewDealView(FormView):
	template_name = 'deals/add_new_deal.html'
	form_class = AddNewDealForm

	def get_form(self, form_class=None):
		form = super(AddNewDealView, self).get_form(form_class)
		form.fields['category_id'].choices = (Category.objects.
			all().values_list('id', 'category_name'))
		form.fields['tag_id'].choices = (Tag.objects.
			all().values_list('id', 'tag_name'))
		return form

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save(request)
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def get_success_url(self):
		return reverse('home')


