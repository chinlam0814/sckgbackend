from django.db import models
from django.contrib.auth.models import User

class Account(User):
    join_date = models.DateField(auto_now_add=True, null=True)
    gender = models.CharField(default='man', max_length=7)

    def __str__(self):
        return self.username
    
    def body(self):
        return {
            'id' : self.id,
            'user' : 'Account',
            'username' : self.username,
            'password' : self.password,
            'join_date' : self.join_date,
            'gender' : self.gender,
        }
    
    class Meta:
        verbose_name = 'Account'

class Admin(User):
    join_date  = models.DateField(auto_now_add=True, null=True)
    gender = models.CharField(default='man', max_length=7)

    def __str__(self):
        return self.username
    
    def body(self):
        return {
            'id' : self.id,
            'user' : 'Admin',
            'username' : self.username,
            'password' : self.password,
            'join_date' : self.join_date,
            'gender' : self.gender,
        }
    
    class Meta:
        verbose_name = 'Admin'
