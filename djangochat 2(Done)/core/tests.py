from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class CoreViewTests(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def test_frontpage_view(self):
        response = self.client.get(reverse('frontpage'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_GET(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_POST_valid_form(self):
        data = {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)  

    def test_user_list_view(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)

    def test_private_messages_view_GET(self):
        response = self.client.get(reverse('private_messages', args=['testuser']))
        self.assertEqual(response.status_code, 302)

    def test_individual_chats_view(self):
        response = self.client.get(reverse('individual_chats'))
        self.assertEqual(response.status_code, 302)

'''from django.test import TestCase

from django.test import  TestCase
from django.urls import reverse


class CoreViewsTest(TestCase):
     # Test the frontpage view
    def test_frontpage_view(self):
        # Send a GET request to the 'frontpage' URL
        response = self.client.get(reverse('frontpage'))
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the text "Djangochat"
        self.assertContains(response, "Djangochat")
        
    # Test the individual_chats view
    def test_individual_chats_view(self):
        response = self.client.get(reverse('individual_chats'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Individual Chats")
        
    # Test the user_list view
    def test_user_list_view(self):
        # Log in with a test user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the text "User List"
        self.assertContains(response, "User List")'''
