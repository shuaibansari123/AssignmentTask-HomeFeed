from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Parent(models.Model):
    name = models.CharField(max_length = 255 , null=False , blank=False)
    age = models.IntegerField()
    gender = models.CharField(choices = [ 
                ('male' , 'male') ,
                ('female' , 'female') ] , max_length = 255
            )
    parent_type = models.CharField(choices = [
                ('first-time parent' , 'first-time parent') ,
                ('experienced parent' , 'experienced parent') ,
            ] , max_length = 255
            )

    # we can override __str__ , __repr__ , manager also


class Child(models.Model):
    parent = models.ForeignKey(Parent , related_name='children', on_delete=models.CASCADE , null=False , blank=False)
    name = models.CharField(max_length = 255 , null=False , blank=False)
    age = models.IntegerField()
    gender = models.CharField(choices = [
                ('male' , 'male') ,
                ('female' , 'female')] , max_length = 255 
            )
        
        
class Blog(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , null=False , blank=False)
    title = models.CharField(max_length = 555 , null=False , blank=False)
    blog_description = models.CharField(max_length = 555 , null=False , blank=False)

    content_age = models.IntegerField()
    content_gender = models.CharField(choices = [
                ('male' , 'male') ,
                ('female' , 'female')] , max_length = 255
            )

