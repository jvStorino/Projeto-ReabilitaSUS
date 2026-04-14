from django.test import TestCase
from .models import Contato


class ContatoModelTest(TestCase):
    def test_criar_contato(self):
        contato = Contato.objects.create(
            nome='Teste',
            email='teste@example.com',
            mensagem='Mensagem de teste.'
        )
        self.assertEqual(contato.nome, 'Teste')
        self.assertEqual(contato.email, 'teste@example.com')
        self.assertIn('teste', contato.mensagem)
