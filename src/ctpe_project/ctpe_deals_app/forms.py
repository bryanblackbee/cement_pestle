from django.forms import Form, ModelForm
from django.forms import ChoiceField

from django.forms import formset_factory

from ctpe_deals_app.models import Deal


class ChooseCategoryForm(Form):
	category_id = ChoiceField(label='Category')


class AddDealForm(ModelForm):
	class Meta:
		model = Deal
		fields = ['deal_name', 'deal_text']


# Formsets #####
AddDealsFormset = formset_factory(AddDealForm, extra=1, 
	min_num=1, max_num=5)