from django.contrib.auth.models import User
from django.db import models

from member.models import Member
from model.models import Period


class Friend(Period):
    FRIEND_CHOICES = [
        (-1, '거절'),
        (0, '대기'),
        (1, '승인')
    ]

    sander = models.ForeignKey(Member, related_name='sender_set', on_delete=models.PROTECT, null=False)
    receiver = models.ForeignKey(Member, related_name='receiver_set', on_delete=models.PROTECT, null=False)
    status = models.IntegerField(choices=FRIEND_CHOICES, default=0)

    class Meta:
        db_table = 'tbl_friend'
