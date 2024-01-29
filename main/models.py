from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """
    Модель выражающая ученика учителя(для цитат)
    """
    name = models.CharField(max_length=30, help_text="Enter a name")
    surname = models.CharField(max_length=30, help_text="Enter a surname")
    graduateDate = models.DateField(help_text="Enter a date of graduation")
    quote = models.CharField(max_length=200, help_text="Enter a quote of student")

    def __str__(self):
        # Cтрока из записи в базе для отображения в админке
        return str(self.name) + " " + str(self.surname)


def validate_percent(value):
    # провека что значения процента укладываются в их диапозон
    if value > 100 or value < 0:
        raise ValidationError("value cant be percent")


class Results(models.Model):
    percentage = models.IntegerField(help_text="Enter a test result",
                                     validators=[validate_percent])
    finishedDate = models.DateTimeField(help_text="Enter a date when text finished")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.percentage) + " " + str(self.user)
