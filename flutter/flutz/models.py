from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):

    each_member = models.OneToOneField(User)


class Post(models.Model):

    flutt = models.TextField(max_length=140)
    flutter_user = models.ForeignKey(Member, related_name='user', null=False)
    post_time = models.DateField(auto_now=True)

