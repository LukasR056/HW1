from django.db import models

# Create your models here.
class Country(models.Model):

    name = models.TextField()

    # TODO: implement __str__ method
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class Club(models.Model):

    name = models.TextField()
    founding_date = models.DateField()
    points = models.PositiveIntegerField()
    active = models.BooleanField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    players = models.ManyToManyField('Player')

    # TODO: implement __str__ method
    def __str__(self):
        return self.name


class Player(models.Model):
    CHOICES = (
        ('g', 'goalkeeper'),
        ('d', 'defender'),
        ('m', 'midfielder'),
        ('s', 'striker')
    )

    first_name = models.TextField()
    last_name = models.TextField()
    year_of_birth = models.IntegerField()
    scorrer_points = models.PositiveIntegerField(help_text="Goals and Asissts")


    # TODO: implement __str__ method
    def __str__(self):
        return self.first_name + ' ' + self.last_name
