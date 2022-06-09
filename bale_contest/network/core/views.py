from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response 
from rest_framework import status 
from .models import CustomeUser, Post
from rest_framework.decorators import api_view
from .serializers import UserSerializer


@api_view(['GET'])
def users_view(request):
    users = CustomeUser.objects.all()
    serialized_users = UserSerializer(users, many=True)
    print(serialized_users.data)
    return Response(serialized_users.data)


@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    if username:
        user = CustomeUser.objects.create_user(username)
    else:
        return Response({'error': 'username must be set.'})
    return Response({'user_id': str(user.id)})


@api_view(['POST'])
def publish_view(request):
    user_id = int(request.META.get('user_id'))
    message = request.data.get('message')
    print(user_id, message)
    if user_id:
        user = get_object_or_404(CustomeUser, id=user_id)
    else:
        return Response({'error': 'user_id must be defined in the header.'})

    if not message:
        return Response({'error': 'message can not be empty.'})

    post = Post.objects.create(message=message, user=user)
    print(user.posts.all())
    return Response({'success': 'post as published successfully.'})
    

@api_view(['POST'])
def follow_view(request):
    user_id = int(request.META.get('user_id'))
    target_username = request.data.get('username')
    user = get_object_or_404(CustomeUser, id=user_id)
    target = get_object_or_404(CustomeUser, username=target_username)
    if target not in user.following.all():
        user.following.add(target)
        return Response({'success': f'{target_username} is being followed.'})
    else:
        return Response({'error': f'{target_username} is already being followed.'})

@api_view(['GET'])
def get_timeline(request):
    user_id = request.META.get('user_id')
    user = get_object_or_404(CustomeUser, id=user_id)
    timeline = {}
    for following in user.following.all():
        if following.posts.last() is not None:
            timeline[following.username] = following.posts.last().message
        else:
            timeline[following.username] = 'No posts yet.'

    return Response(timeline)