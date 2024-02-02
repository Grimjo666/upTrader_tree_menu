from django.db import models


class TreeMenu(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    url = models.CharField(max_length=150)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title
