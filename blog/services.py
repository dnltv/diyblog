from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from .models import Like

User = get_user_model()


def add_like(obj, user):
    """
    Liked an 'obj'
    """
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)

    return like


def remove_like(obj, user):
    """
    Delete a like from an 'obj'
    """
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def is_fan(obj, user) -> bool:
    """
    Check is 'user' liked an 'obj'
    """
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    )

    return likes.exists()


def get_fans(obj, user):
    """Get all users who have liked an 'obj'"""
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        likes__contenttype_object=obj_type, likes__object_id=obj.id
    )
