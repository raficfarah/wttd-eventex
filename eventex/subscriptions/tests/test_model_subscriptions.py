from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Rafic Farah',
            cpf = '12345678910',
            email = 'raficfarah07@gmail.com',
            phone = '21-99999-9999'
        )
        self.obj.save()
    

    def test_create(self):
        self.assertTrue(Subscription.objects.exists)

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)