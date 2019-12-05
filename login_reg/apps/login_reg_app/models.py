from django.db import models
import datetime, re, bcrypt

class ShowsManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData['first']) < 3:               
            errors["first"] = "Invalid First Name, please try again!"
        if len(postData['last']) < 3:               
            errors["last"] = "Invalid Last Name, please try again!"
        if not EMAIL_REGEX.match(postData['email']):        
            errors['email'] = "Invalid email address!" #might need parentheses
        if Registration.objects.filter(email=postData['email']):
            errors['email'] = 'This email is already being used'
        if len(postData['email']) < 8:               
            errors["email"] = "Invalid email length!"
        if len(postData['password']) < 10:               
            errors["password"] = "Password must be atleast 10 charactors long!"
        if postData['password'] != postData['password_confirmation']: 
            errors['password'] = "Passwords do not match"
        return errors

    def log_val(self, postData):
        errors = {}
        
        if len(postData['email']) < 8:               
            errors["email"] = "Invalid email length!"
        if len(postData['password']) < 10:               
            errors["password"] = "Password must be atleast 10 charactors long!"
        return errors

class Registration (models.Model):

    first_name = models.CharField(max_length=(255))
    last_name = models.CharField(max_length=(255))
    email = models.CharField(max_length=(255))
    password = models.CharField(max_length=(255))
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager() 
    
    
