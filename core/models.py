from django.db import models


class Contato(models.Model):
    nome = models.CharField('Nome', max_length=120)
    email = models.EmailField('E-mail')
    mensagem = models.TextField('Mensagem')
    data_envio = models.DateTimeField('Data de envio', auto_now_add=True)

    class Meta:
        ordering = ['-data_envio']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.nome} - {self.email}'
