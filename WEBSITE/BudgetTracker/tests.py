from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class PublicPageTests(TestCase):
    def test_public_pages_render(self):
        for page in ("home", "about", "features", "contact", "login", "register"):
            with self.subTest(page=page):
                response = self.client.get(reverse(page))
                self.assertEqual(response.status_code, 200)


class RegistrationTests(TestCase):
    def test_valid_registration_creates_and_logs_in_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "budget-user",
                "password1": "Finance!Track8274",
                "password2": "Finance!Track8274",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_mismatched_passwords_do_not_create_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "budget-user",
                "password1": "Finance!Track8274",
                "password2": "Different!Track8274",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="budget-user").exists())
