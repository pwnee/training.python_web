from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):
	"""
	Blog post model includes: title, post, author, and publish date
	"""
	title = models.CharField('title', max_length=200)
	post = models.CharField('post', max_length=2000)
	author = models.ForeignKey(User)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return self.title

from django import forms

