from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from room.models import Message, IndividualChat

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            #login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})

def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'core/user_list.html', {'users': users})

@login_required
def private_messages(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    
    
    # Count the messages for the current user
    total_messages = IndividualChat.objects.filter(sender=request.user, receiver=user).count()
    
    messages = IndividualChat.objects.filter(
    Q(sender=request.user, receiver=user) | Q(sender=user, receiver=request.user)
)
    #messages = IndividualChat.objects.filter(sender=request.user, receiver=user) | IndividualChat.objects.filter(sender=user, receiver=request.user)

    return render(request, 'core/private_messages.html', {'user': user, 'messages': messages, 'total_messages': total_messages})

@login_required
def send_private_message(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        content = request.POST.get('content')
        # Replace with the actual logic to create and save the message
    return redirect('private_messages', username=username)


@login_required
def individual_chats(request):
    return render(request, 'core/individual_chats.html')