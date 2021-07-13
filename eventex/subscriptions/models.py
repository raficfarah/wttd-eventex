from django.db import models
from django.utils.timezone import now


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('data de registro', default=now)
    hash_url = models.CharField('URL', max_length=32, null=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
        