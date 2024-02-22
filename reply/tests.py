from django.test import TestCase

from member.models import Member
from post.models import Post
from reply.models import Reply

import random


class ReplyTest(TestCase):
    # replies = []
    # # 총 98개 댓글 작성하기
    # # 랜덤한 회원을 작성자로 설정하기
    # member_queryset = Member.objects.all()
    # # 랜덤한 게시물을 대상글로 설정하기
    # post_queryset = Post.objects.all()
    #
    # for i in range(98):
    #     reply = {
    #         'reply_content': f"테스트 댓글{i + 1}",
    #         'member': member_queryset[random.randint(0, len(member_queryset)-1)],
    #         'post': post_queryset[random.randint(0, len(post_queryset)-1)]
    #     }
    #     replies.append(Reply(**reply))
    # Reply.objects.bulk_create(replies)

    # 커스텀 문제
    # 나이가 30 이상인 회원이 작성한 댓글의 게시물 제목 및 회원의 이름 조회
    replies = Reply.objects.filter(member__member_age__gte=30, member__member_status=True).values('post__post_title', 'member__member_name', 'member__member_age')

    for reply in replies:
        print(reply)

