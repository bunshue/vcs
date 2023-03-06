from django.db import models

class student(models.Model):
	cName = models.CharField(max_length=20, null=False)
	cSex = models.CharField(max_length=2, default='M', null=False)
	cBirthday = models.DateField(null=False)
	cEmail = models.EmailField(max_length=100, blank=True, default='')
	cPhone = models.CharField(max_length=50, blank=True, default='')
	cAddr = models.CharField(max_length=255,blank=True, default='')
	
	def __str__(self):
		return self.cName
