from django.db import models

# Create your models here.

class urlist(models.Model):
	src_url = models.URLField()
	short_url = models.CharField(max_length=20)
	count = models.PositiveIntegerField()

	def __unicode__(self):
		return self.short_url
