from django.conf import settings
from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Rafic Farah', cpf='00000000000',
                    email='raficfarah07@gmail.com', phone='21-99999-9999')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)


    def test_subscription_email_from(self):        
        expect = settings.DEFAULT_FROM_EMAIL
        self.assertEqual(expect, self.email.from_email)


    def test_subscription_email_to(self):        
        expect = [settings.DEFAULT_FROM_EMAIL, 'raficfarah07@gmail.com']
        self.assertEqual(expect, self.email.to)


    def test_subscription_email_body(self):
        contents = ['Rafic Farah', 
                    '00000000000',
                    'raficfarah07@gmail.com',
                    '21-99999-9999']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)