from django.db import models


class Wordclass(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32, null=True)


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=False)
    wordclass1 = models.ForeignKey(Wordclass, related_name='wordclass1', on_delete=models.CASCADE)
    wordclass2 = models.ForeignKey(Wordclass, related_name='wordclass2', on_delete=models.CASCADE)
    wordclass3 = models.ForeignKey(Wordclass, related_name='wordclass3', on_delete=models.CASCADE)
    wordclass4 = models.ForeignKey(Wordclass, related_name='wordclass4', on_delete=models.CASCADE)
    chinese1 = models.CharField(max_length=32, null=False)
    chinese2 = models.CharField(max_length=32, null=False)
    chinese3 = models.CharField(max_length=32, null=False)
    chinese4 = models.CharField(max_length=32, null=False)
    example = models.CharField(max_length=1000)


class User(models.Model):
    class Mata:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, null=False)
    email = models.CharField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)

    def __repr__(self):
        return "{} {}".format(self.id, self.name)

    __str__ = __repr__


class Bunch(models.Model):
    username_text = models.CharField(max_length=200)
    floors = models.IntegerField(default=0)


class Floor(models.Model):
    bunch = models.ForeignKey(Bunch, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    discuss_text = models.CharField(max_length=200, null=False)
    floor_date = models.DateTimeField('date published')
    motto_text = models.CharField(max_length=200)
