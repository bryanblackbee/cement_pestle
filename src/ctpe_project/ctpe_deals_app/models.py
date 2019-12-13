from django.db import models

# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=256, 
		verbose_name='Category Name')

	def __str__(self):
		return self.category_name

	class Meta:
		verbose_name_plural = 'Categories'


class Tag(models.Model):
	tag_name = models.CharField(max_length=16, verbose_name='Tag Name')

	def __str__(self):
		return self.tag_name		


class Deal(models.Model):
	for_category = models.ForeignKey(Category, null=True, 
		on_delete=models.PROTECT)
	deal_name = models.CharField(max_length=512, verbose_name='Deal Name')
	deal_text = models.TextField(verbose_name='Deal Text')
	has_tag = models.ManyToManyField(Tag, blank=True)

	def __str__(self):
		return self.deal_name