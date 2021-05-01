from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to="personal_portfolio/images/")
	github_url = models.URLField
	heroku_url = models.URLField(blank=True)
