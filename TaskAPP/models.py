from django.db import models

# Create your models here.


class Task(models.Model):
	task_name = models.CharField(max_length=20)
	task_desc = models.CharField(max_length=30)
	date_created = models.DateTimeField(auto_now=True)
	completed = models.BooleanField(default=False)
	image = models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
	doc = models.FileField(upload_to='Doc/',default='Doc/None/No-doc.pdf')

	def __str__(self):
		return " %s " % self.task_name

