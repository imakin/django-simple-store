from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from store import models

# Create your tests here.
class OrderingTestCase(TestCase):
    def setUp(self):
        models.Storesetting.objects.create(name='price_currency', value='IDR')
        models.Storesetting.objects.create(name='price_multiplier', value='1000')
        models.Storesetting.objects.create(name='fake_user_email_domain', value='izzulmakin.com')
        
        self.email_domain = models.Storesetting.objects.get(name='fake_user_email_domain').value
        User.objects.create_user('makin', '085000000000@'+self.email_domain, 'testpassword')
    
    
    def test_customer(self):
        test_user = authenticate(username='makin', password='testpassword')
        test_user_phone = test_user.email.replace("@"+self.email_domain, "")
        self.assertIsNotNone(test_user)
        models.Customer.objects.create(
            user=test_user,
            phone_number=test_user_phone,
        )
