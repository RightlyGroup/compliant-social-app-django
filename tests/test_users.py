from unittest.mock import MagicMock

from django.test import TestCase
from django.contrib.auth import get_user_model

from compliant_social_django.models import UserSocialAuth


class TestUsers(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='randomtester', email='user@example.com')
        self.usa = UserSocialAuth.objects.create(
            user=self.user, provider='my-provider', uid='1234')

    def test_user_social_auth_actual_refresh_token_persists_after_calling_refresh_token(self):
        mock_backend = MagicMock()
        self.usa.get_backend_instance = MagicMock()
        self.usa.get_backend_instance.return_value = mock_backend
        mock_backend.extra_data.return_value = {'access_token': '123'}

        old_access_token = self.usa.actual_access_token
        old_refresh_token = self.usa.actual_refresh_token

        self.usa.refresh_token(MagicMock())

        new_access_token = '123'
        new_refresh_token = self.usa.actual_refresh_token

        self.assertEqual(old_refresh_token, new_refresh_token)
        self.assertNotEqual(old_access_token, new_access_token)

    def test_access_token_is_set_to_none_if_access_token_is_not_present_in_response(self):
        mock_backend = MagicMock()
        self.usa.get_backend_instance = MagicMock()
        self.usa.get_backend_instance.return_value = mock_backend
        mock_backend.extra_data.return_value = {}

        self.usa.refresh_token(MagicMock())

        self.assertIsNone(self.usa.actual_access_token)