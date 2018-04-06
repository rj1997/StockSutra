from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


#class StockUser(models.Model):
#	name = models.CharField(max_length=100)
#	email = models.EmailField(max_length=100)
#	contact = models.CharField(max_length=100)
#	portfolio = EmbeddedModelField('StockList')
    


# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100,blank=True)
    AAPLvalue = models.IntegerField(blank=True,default=0,null=True)
    CSCOvalue = models.IntegerField(blank=True,default=0,null=True)
    CATvalue = models.IntegerField(blank=True,default=0,null=True)
    BAvalue = models.IntegerField(blank=True,default=0,null=True)
    CVXvalue = models.IntegerField(blank=True,default=0,null=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=20000)
    user =  models.CharField(max_length=200)
    comment = models.CharField(max_length=20000,blank=True)
    comment_user = models.CharField(max_length=200,blank=True)




for user in UserProfile.objects.all():
    print(user)








class StockList(models.Model):
	#pass
	stockname = models.CharField(max_length=100)
	buyprice = models.FloatField()
	buydate = models.DateTimeField()
	
