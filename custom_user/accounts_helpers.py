from .models import Profile

from google.oauth2 import id_token
from google.auth.transport import requests

from django.core.exceptions import ObjectDoesNotExist
# def delete_user_sessions(user):
#     user_sessions = UserSession.objects.filter(user=user)
#     for user_session in user_sessions:
#         user_session.session.delete()


def get_user_by_token(token):
    email = get_email_from_token(token)
    if email is not None:
        try:
            user = Profile.objects.get(email=email)
            return user
        except ObjectDoesNotExist:
            return None
    return None

def get_email_from_token(idToken):
    idinfo = verify_token(idToken)
    if idinfo is not None:
        return idinfo['email']
    else:
        return None

def verify_token(token):
    CLIENT_ID = '942480069892-05kgachoktolijpd718lpna2smq6rsdk.apps.googleusercontent.com'
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
    return idinfo