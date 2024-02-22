from django.db.models import Q
from django.test import TestCase

from member.models import Member


class MemberTest(TestCase):
    # 클래스 내부에 코드를 작성하면 연결한 테이블에 저장되고,
    # 메소드 내에서 코드를 작성하면 임시 테이블에 저장된 뒤 사라진다.

    # create
    member = Member.objects.create(
        member_email='test1@gmail.com',
        member_password='1234',
        member_age=20,
        member_name='테스트1',
    )

    print(member.__dict__)
    # def test_member_creation(self):
    #     member = Member.objects.create(
    #         member_email='test1@gmail.com',
    #         member_password='1234',
    #         member_age=20,
    #         member_name='테스트1',
    #     )
    #
    #     print(member.__dict__)

    # 회원 1명 추가
    Member.objects.create()

    # 회원 2명 추가
    for i in range(2):
        Member.objects.create()

    # save
    datas = {
        'member_email': 'test2@gmail.com',
        'member_password': '1234',
        'member_age': 20,
        'member_name': '테스트2',
    }
    member = Member(**datas)
    member.save()

    # 회원 1명 추가
    datas = {}
    member = Member(**datas)
    member.save()

    # 회원 2명 추가
    datas = [
        {},
        {},
    ]

    for data in datas:
        member = Member(**data)
        member.save()

    # bulk_create
    # id는 가져오지 않는다.
    members = Member.objects.bulk_create([
        Member(
            member_email='test3@gmail.com',
            member_password='1234',
            member_age=10,
            member_name='테스트3'),
        Member(
            member_email='test4@gmail.com',
            member_password='1234',
            member_age=30,
            member_name='테스트4'),
        Member(
            member_email='test5@gmail.com',
            member_password='1234',
            member_age=40,
            member_name='테스트5')
    ])

    for member in members:
        print(member.__dict__)

    # 회원 2명 추가
    datas = [
        {},
        {}
    ]

    members = []

    for data in datas:
        members.append(Member(**data))

    Member.objects.bulk_create(members)

    # get_or_create
    datas = {
        'member_password': '1234',
        'member_age': 50,
        'member_name': '테스트6',
    }
    member, created = Member.objects.get_or_create(member_email='test6@gmail.com', defaults=datas)
    print(member.__dict__, created)

    # member_email이 'admin1@gmail.com'인 회원을 조회한다.
    # 만약 없으면 새로운 정보를 전달하여 회원을 추가한다.
    datas = {}

    member, isCreated = Member.objects.get_or_create(member_email='admin1@gmail.com', defaults=datas)

    # get
    member = Member.objects.get(id=3)
    print(member.__dict__)

    # all
    members = Member.objects.all()
    members = Member.enabled_objects.all()
    for member in members:
        print(member.__dict__)

    # filter
    member_queryset = Member.enabled_objects.filter(member_name='테스트6')
    print(member_queryset.exists())
    print(member_queryset[0].__dict__)

    # contains
    member_queryset = Member.enabled_objects.filter(member_name__contains='테')
    print(member_queryset.exists())
    for member in member_queryset:
        print(member.__dict__)

    # startswith, endswith
    member_queryset = Member.enabled_objects.filter(member_name__startswith='테')
    print(member_queryset.exists())
    for member in member_queryset:
        print(member.__dict__)
    member_queryset = Member.enabled_objects.filter(member_name__endswith='3')
    print(member_queryset.exists())
    for member in member_queryset:
        print(member.__dict__)

    # in
    member_queryset = Member.enabled_objects.filter(member_email__in=['test3@gmail.com', 'test6@gmail.com']).values('member_email')
    print(member_queryset.query)
    for member in member_queryset:
        print(member.get('member_email'))

    # exclude()
    member_queryset = Member.enabled_objects.exclude(member_email='test3@gmail.com').values('member_email')
    for member in member_queryset:
        print(member["member_email"])

    # AND, OR
    member_queryset = Member.objects.filter(status=True) & Member.objects.filter(member_age__gt=30)
    condition1 = Q(status=True)
    condition2 = Q(member_age__gt=30)
    member_queryset = Member.objects.filter(condition1 & condition2)
    member_queryset = Member.objects.filter(condition1 | condition2)
    for member in member_queryset:
        print(member.member_email, member.member_age, sep=", ")

    # order_by
    member_queryset = Member.objects.all().order_by('-id')
    for member in member_queryset:
        print(member.__dict__)