from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),

)



class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Bug(models.Model):
    name = models.CharField(max_length=100)
    type_bug = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
# Create your models here.

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bug_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Feed Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        
        )

    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for bug_id: {self.bug_id} @{self.url}"

class Meta:
    ordering = ['-date']