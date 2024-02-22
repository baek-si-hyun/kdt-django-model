from django.test import TestCase
from random import randint

from member.models import Member
from post.models import Post


class PostTest(TestCase):
    # posts = []
    # # 랜덤한 회원을 작성자로 설정하기
    # member_queryset = Member.objects.all()
    # # 총 98개 게시글 작성하기
    # for i in range(98):
    #
    #     post = {
    #         'post_title': f'테스트 제목{i + 1}',
    #         'post_content': f'테스트 내용{i + 1}',
    #         'member': member_queryset[randint(0, len(member_queryset) - 1)]
    #     }
    #     # 트러블 슈팅
    #     # Code: posts.append(post)
    #     # Error: AttributeError: 'dict' object has no attribute 'pk'
    #
    #     # dict객체를 Django ORM에 전달하면 정확히 인식이 안되었다.
    #     # 이를 모델 객체에 담아서 전달하니 정확이 인식되었다.
    #
    #     posts.append(Post(**post))
    #
    # Post.objects.bulk_create(posts)

    # 로그인된 회원의 마이페이지에서 내가 작성한 게시글 조회하기
    # member = Member.objects.get(member_status=True, id=3)
    # for post in member.post_set.all():
    #     print(post)

    # 나이가 30 미만인 회원이 작성한 게시글 목록 조회
    # members = Member.objects.filter(member_age__lt=30)
    #
    # for member in members:
    #     posts = Post.objects.filter(member=member)
    #     # print(member.__dict__)
    #     for post in posts:
    #         # 단, 회원의 이름과 회원의 나이까지 같이 조회하기
    #         print(post.post_title, post.post_content, post.member.member_name, post.member.member_age, sep=', ')

    # 나이가 30 미만인 회원이 작성한 게시글 목록 조회
    # posts = Post.objects.filter(member__member_age__lt=30, member__member_status=True).values('member__member_age',
    #                                                                                           'member__member_name',
    #                                                                                           'post_title',
    #                                                                                           'post_content',
    #                                                                                           'created_date',
    #                                                                                           'updated_date')
    # for post in posts:
    #     print(post)

    # 회원의 나이가 20이상 30이하인 회원이 작성한 게시글 중 post_title에 "테"가 들어가고 내용에 "7"로 끝나는 게시글 정보 조회
    # Member는 사용하지 않고 Post만 사용해서 하기
    # 나이 범위는 __range를 사용해서 진행

    posts = Post.objects.filter(member__member_age__range=(20, 30), post_title__contains='te',
                                post_content__endswith='7').values('member__member_age')

    for post in posts:
        print(post)
