from django.db import models


# class KontentorDeal(models.Model):
#     """
#     Сделка
#     """

#     name = models.CharField(max_length=150)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     amount = models.DecimalField(max_digits=None, decimal_places=None)
#     # currency

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Сделка"
#         verbose_name_plural = "Сделки"
