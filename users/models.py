from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    test = models.CharField(max_length=20, default="")
    test2 = models.CharField(max_length=20, null=True)
    first_name = None  # 이 필드가 제외되어야 하는 경우 이대로 두시면 됩니다.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nickname = models.CharField(max_length=10, null=True, blank=True)  # 빈 문자열 허용
    image = models.ImageField(upload_to='profile/', null=True, blank=True)  # 빈 파일 허용
    bio = models.TextField(default="")  # 기본값을 빈 문자열로 설정

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.nickname if self.nickname else "Unnamed"  # nickname이 None이면 "Unnamed" 반환

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # 사용자 생성 시 프로필 자동 생성
