from django.db import models


# Create your models here.
class Airtel(models.Model):
    airtel_plan = models.CharField(max_length=10)
    airtel_plan1 = models.CharField(max_length=10)
    airtel_plan2 = models.CharField(max_length=10)
    airtel_plan3 = models.CharField(max_length=10)

    def __str__(self):
        return str(self)


class Jio(models.Model):
    jio_plan = models.CharField(max_length=10)
    jio_plan1 = models.CharField(max_length=10)
    jio_plan2 = models.CharField(max_length=10)
    jio_plan3 = models.CharField(max_length=10)

    def __str__(self):
        return str(self)


class Idea(models.Model):
    idea_plan = models.CharField(max_length=10)
    idea_plan1 = models.CharField(max_length=10)
    idea_plan2 = models.CharField(max_length=10)
    idea_plan3 = models.CharField(max_length=10)

    def __str__(self):
        return str(self)


class Bsnl(models.Model):
    bsnl_plan = models.CharField(max_length=10)
    bsnl_plan1 = models.CharField(max_length=10)
    bsnl_plan2 = models.CharField(max_length=10)
    bsnl_plan3 = models.CharField(max_length=10)

    def __str__(self):
        return str(self)


class Operator(models.Model):
    airtel = models.ForeignKey(Airtel, on_delete=models.SET_NULL, null=True, blank=True)
    jio = models.ForeignKey(Jio, on_delete=models.SET_NULL, null=True, blank=True)
    idea = models.ForeignKey(Idea, on_delete=models.SET_NULL, null=True, blank=True)
    bsnl = models.ForeignKey(Bsnl, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.airtel) + " | " + str(self.jio) + " | " + str(self.idea) + " | " + str(self.bsnl)


class User(models.Model):
    user_number = models.CharField(max_length=10)
    Operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self)
