from .models import UserProfile
from django.contrib.auth.models import User

def save_profile(backend, user, response, *args, **kwargs):
    #print("user profile")
    #print(user.username)
    #print(user.id)
    #print(UserProfile.objects.filter(user_id=user.id).exists())
    if(UserProfile.objects.filter(user_id=user.id).exists()):
        pass
    else:
        UserProfile.objects.create(
            user=user,
            profile_photo_url = response['picture']
        )
        print("user profile new")
