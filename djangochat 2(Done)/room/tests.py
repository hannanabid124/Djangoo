from django.test import TestCase
from asgiref.testing import ApplicationCommunicator
from room.consumers import ChatConsumer, IndivConsumer
from django.test import Client, TestCase
from django.urls import reverse
from channels.testing import WebsocketCommunicator
from room.models import Message
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
import pytest
from room.models import Room


@pytest.mark.asyncio
async def test_join_individual_chat():
    communicator = ApplicationCommunicator(IndivConsumer, {'type': 'websocket.connect', 'path': '/ws/testuser/'})
    connected, _ = await communicator.connect()

    assert connected

    await communicator.disconnect()
    

class RoomViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.another_user = User.objects.create_user(username='anotheruser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.room = Room.objects.create(name='Test Room', slug='test-room')
        self.message = Message.objects.create(room=self.room, user=self.user, content='Hello, World!')

    def test_user_list_view(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User List")
        
class RoomViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.room = Room.objects.create(name='Test Room', slug='test-room')

    def test_rooms_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('rooms'))
        self.assertEqual(response.status_code, 200)

    def test_room_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('room', args=['test-room']))
        self.assertEqual(response.status_code, 200)