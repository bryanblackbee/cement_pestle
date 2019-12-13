from django.forms import Form, ModelForm, Textarea
from django.forms import ChoiceField
from django.forms import formset_factory
from django.db import IntegrityError, transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
	Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit)

from ctpe_deals_app.models import Deal, Category, Tag
from .form_layouts import (CustomAddDealsFormset)


class AddMultipleDealsForm(Form):
	category_id = ChoiceField(label='Category')

	def __init__(self, *args, **kwargs):
		super(AddMultipleDealsForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = True
		self.helper.layout = Layout(
			Div(
				Field('category_id'),
				CustomAddDealsFormset('deals'),
				HTML('<hr>'),
				ButtonHolder(Submit('submit', 'Add Deals', css_class='btn btn-success')),
			))


class AddNewDealForm(ModelForm):
	category_id = ChoiceField(label='Category')
	tag_id = ChoiceField(label='Tags')

	class Meta:
		model = Deal
		fields = ['deal_name', 'deal_text']
		widgets = {'deal_text' : Textarea(attrs={'cols': 40, 'rows': 3})}

	def __init__(self, *args, **kwargs):
		super(AddNewDealForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = True
		self.helper.layout = Layout(
			Div(
				Div(
					Div('category_id', css_class="col-md-4"),
					css_class="row"),
				Div(
					Div('deal_name', css_class="col-md-10"),
					Div('deal_text', css_class="col-md-10"),
					css_class="row"),
				Div(
					Div('tag_id', css_class="col-md-4"),
					css_class="row"),
				ButtonHolder(Submit('submit', 'Add Deal', css_class='btn btn-success'))
			))

	def save(self, request):
		sel_category_id = self.cleaned_data.get('category_id', None)
		sel_tag = self.cleaned_data.get('tag_id', None)
		sel_deal_name = self.cleaned_data.get('deal_name')
		sel_deal_text = self.cleaned_data.get('deal_text')

		category = Category.objects.get(id=sel_category_id)
		tag = Tag.objects.get(id=sel_tag)

		try:
			with transaction.atomic():
				deal = Deal(for_category=category, deal_name=sel_deal_name, 
					deal_text=sel_deal_text)
				print(deal)
				print(deal.for_category)
				deal.save(force_insert=True, force_update=False)
				deal.has_tag.add(tag)
				deal.save()
		except IntegrityError:
			raise forms.ValidationError("ATOMIC TRANSACTION ERROR: Please try again.")		
		super(AddNewDealForm, self).save()



class AddDealForm(ModelForm):
	class Meta:
		model = Deal
		fields = ['deal_name', 'deal_text']
		widgets = {'deal_text' : Textarea(attrs={'cols': 40, 'rows': 3})}


# Formsets #####
AddDealsFormset = formset_factory(AddDealForm, extra=2, 
	min_num=1, max_num=5)