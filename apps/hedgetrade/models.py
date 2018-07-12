from django.db import models

# Create your models here.
class HedgeOrder(models.Model):
    site1 = models.CharField('site1', max_length = 255)
    site2 = models.CharField('site2', max_length = 255)

    class Meta:
        verbose_name = "对冲订单"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.site1 + self.site2