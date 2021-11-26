from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UserAccountTests(TestCase):
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
                'testuser@super.com', 'username', 'firstname', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.username, 'username')
        self.assertEqual(super_user.nome, 'firstname')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "nome")

        with self.assertRaises(TypeError):
            db.objects.create_superuser(
                email='testuser@super.com', username="username1", nome="firstname", password="password", is_superuser=False
            )

        with self.assertRaises(TypeError):
            db.objects.create_superuser(
                email='testuser@super.com', username="username1", nome="firstname", password="password", is_superuser=True
            )

        with self.assertRaises(TypeError):
            db.objects.create_superuser(
                email='', username="username1", nome="firstname", password="password", is_superuser=False
            )

    def test_new_user(self):
        db = get_user_model()
        super_user = db.objects.create_user(
                'testuser@super.com', 'username', 'firstname', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.username, 'username')
        self.assertEqual(super_user.nome, 'firstname')
        self.assertFalse(super_user.is_superuser)
        self.assertFalse(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "nome")

        with self.assertRaises(TypeError):
            db.objects.create_user(
                email='', username='a', nome='nome', password='password'
            )