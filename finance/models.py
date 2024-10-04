from django.db import models
from django.contrib.auth.models import User

# Create your models here. The models represent the objects and the endpoints in the API
CATEGORY_CHOICES = [
    ('Food','Food'),
    ('Travel','Travel'),
    ('Rent','Rent'),
    ('Miscellaneous','Miscellaneous')
]
class Expense(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES)
    amount = models.DecimalField(max_length = 10, decimal_places = 2 )
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.category}:{self.amount}"

class Income(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    source = models.CharField(max_length = 100)
    amount = models.DecimalField(decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.source} : {self.amount}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES)
    amount = models.DecimalField(max_length = 10, decimal_places = 2)
    month = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.category} : {self.amount}"

class SavingGoal(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    goal_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    current_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    target_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - Goal : {self.goal_amount}"
    
# models analogous to the various endpoints



