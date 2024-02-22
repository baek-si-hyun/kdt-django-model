from django.db import models
from model.models import Period
from post.models import Post
from member.models import Member


class Reply(Period):
    SECRET_STATUS = [
        ('Y', '비공개'),
        ('N', '공개')
    ]
    reply_content = models.CharField(blank=False, null=False, max_length=100)
    member = models.ForeignKey(Member, null=False, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, null=False, on_delete=models.PROTECT)
    group = models.IntegerField(null=False, default=0)
    depth = models.IntegerField(null=False, default=0)
    secret = models.CharField(choices=SECRET_STATUS, null=False, default='N', max_length=20)

    class Meta:
        db_table = 'tbl_reply'
        ordering = ['-id']

    def __str__(self):
        return self.reply_content
