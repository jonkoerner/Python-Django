from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(model.Manager):
    def validate_login(self, post):
        user = User.objects.filter(email=post["email"]).first()
        if user and bcrypt.checkpw(post['password'].encode(), user.password.encode()):
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'error': "Invalid credentials"}

    def validate_registration(self, post):
        errors = []
        if post['name'] == '':
            errors.append('Name cannot be blank')
        if post['email'] == '':
            errors.append('Email cannot be blank')
        user = User.objects.filter(email=post['email']).first()
        if user:
            errors.append('Email already in use')
        if len(post['password']) < 4:
            errors.append('Password must be at least 4 characters')
        elif post['password'] != post['password_confirmation']:
            errors.append('Passwords must match')
        if not errors:
            user = User.objects.create(
                name=post['name'],
                email=post['email'],
                password=bcrypt.hashpw(
                    post['password'].encode(), bcrypt.gensalt(10))
            )
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'errors': errors}

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
