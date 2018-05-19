from __future__ import unicode_literals

from django.db import models
from ..loginreg.models import User

# Create your models here.

class QuoteManager(models.Manager):
    
    def validateQuote(self, quoted_bynow, message, current_user):
        errors = []

        if len(quoted_bynow) < 1:
            errors.append("Name is required")
        elif len(quoted_bynow) < 3:
            errors.append("Name must be longer than 3 char")

        if len(message) < 1:
            errors.append("Quote is required")
        elif len(message) < 10:
            errors.append("Quote must be longer than 10 char")

        if len(errors) < 1:
            Quote.objects.create(quoted_by=quoted_bynow, quote=message, posted_by=current_user)
        if len(errors) > 1:
            return(  )



        

class Quote(models.Model):
    quoted_by = models.CharField(max_length=255)
    quote = models.CharField(max_length=2000)
    posted_by = models.ForeignKey(User, related_name="quotes")
    follower = models.ManyToManyField(User, related_name="liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()
