from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=255,null=False)
    password=models.CharField(max_length=255,null=False)
    emailaddress=models.EmailField(max_length=255,null=False)
    
    def __str__(self):
        return self.username
        

