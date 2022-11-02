from django.db import models


class Division(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    salary = models.PositiveIntegerField()
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField()
    child_id = models.PositiveIntegerField()

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.patronymic)