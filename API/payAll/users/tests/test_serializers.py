from allauth.account.adapter import get_adapter 
from django.test import TestCase
from users.models import CustomUser

class CustomRegistrationSerializerTest(TestCase):

    def create_user(self, first_name="test", last_name="test", email="test@test.com"):
        return CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, password=123456)

    def test_registration_request(self):
        w = self.create_user()
        self.assertTrue(isinstance(w, CustomUser))
        self.assertEqual(w.__str__(), w.email)