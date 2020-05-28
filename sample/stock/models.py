from django.db import models


class Items(models.Model):
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)
