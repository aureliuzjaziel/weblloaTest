from django.db import models


class VisitCounter(models.Model):
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "visita"
        verbose_name_plural = "visitas"

    def __str__(self):
        return f"Visitas: {self.count}"
