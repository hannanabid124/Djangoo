from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    total_messages = messages.count()  # Count the total messages in the room

    return render(request, 'room/room.html', {'room': room, 'messages': messages, 'total_messages': total_messages})
