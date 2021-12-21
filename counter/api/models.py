from django.db import models


class BaseModel(models.Model):
    date = models.DateField(verbose_name='Дата')
    views = models.PositiveIntegerField(verbose_name='Просмотры',
                                        null=True,
                                        blank=True)
    clicks = models.PositiveIntegerField(verbose_name='Клики',
                                         null=True,
                                         blank=True)
    cost = models.DecimalField(verbose_name='Цена',
                               max_digits=19,
                               decimal_places=2,
                               null=True,
                               blank=True)
    cpc = models.DecimalField(verbose_name='Средняя стоимость клика',
                              max_digits=19,
                              decimal_places=2,
                              null=True,
                              blank=True)
    cpm = models.DecimalField(verbose_name='Средняя стоимость 1000 показов',
                              max_digits=19,
                              decimal_places=2,
                              null=True,
                              blank=True)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
        ordering = ('date', )

    def save(self, *args, **kwargs):
        cpc = cpm = None
        if self.cost and self.clicks:
            cpc = float(self.cost) / float(self.clicks)
        if self.cost and self.views:
            cpm = float(self.cost) / float(self.views) * 1000

        self.cpc = cpc
        self.cpm = cpm
        super().save(*args, **kwargs)
