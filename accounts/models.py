from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_CHOICES = (
        ('trainer', 'Trainer'),
        ('student', 'Student'),
    )

    phone = models.CharField(max_length=15)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

class StudentProfile(models.Model):

    skills = models.CharField(max_length=200, null=True)
    qualification = models.CharField(max_length=200, null=True)
    passout_year = models.CharField(max_length=20, null=True)
    github_url = models.URLField(null=True)
    linkedin_url = models.URLField(null=True)

    student = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student"
    )


class TrainerProfile(models.Model):

    qualification = models.CharField(max_length=200, null=True)
    experience = models.IntegerField(null=True)
    skills = models.CharField(max_length=200, null=True)

    trainer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="trainer"
    )