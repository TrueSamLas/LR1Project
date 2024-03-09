from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    price = models.FloatField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Orders(models.Model):
    date = models.DateTimeField(blank=False)
    service = models.ForeignKey('Services', related_name='orders_services', on_delete=models.CASCADE)
    comment = models.TextField(max_length=100,blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='orders_users', on_delete=models.CASCADE)


    class Meta:
        ordering = ['date']
        verbose_name = "Прием"
        verbose_name_plural = "Приемы"
