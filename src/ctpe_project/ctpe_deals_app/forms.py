from django.forms import Form, ModelForm, Textarea
from django.forms import ChoiceField
from django.forms import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Field, Div, HTML, ButtonHolder, Submit)

from ctpe_deals_app.models import Deal
from .form_layouts import CustomAddDealsFormset


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


class AddDealForm(ModelForm):
	class Meta:
		model = Deal
		fields = ['deal_name', 'deal_text']
		widgets = {'deal_text' : Textarea(attrs={'cols': 40, 'rows': 3})}


# Formsets #####
AddDealsFormset = formset_factory(AddDealForm, extra=2, 
	min_num=1, max_num=5)