from django.db import models


class NodeInfo(models.Model):
    dc_name = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)
    port = models.IntegerField()

    def __str__(self):
            return self.dc_name

