from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator , MaxValueValidator
class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(75)],
                                           null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    STATUS_CHOICES=(
        ('gold','gold'),
        ('silver','silver'),
        ('bronze','bronze'),
        ('simple','simple')

    )
    status = models.CharField(choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}'
