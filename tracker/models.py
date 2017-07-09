from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=2000, blank=True, null=True, default='')
	progress = models.FloatField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title

class Task(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	severity = models.SmallIntegerField()
	open_date = models.DateTimeField()
	close_date = models.DateTimeField()
	status = models.SmallIntegerField(default=0)

	def __str__(self):
		return self.title


# Create your models here.
