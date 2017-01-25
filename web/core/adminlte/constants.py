# coding=utf-8



DEFAULT_DASHBOARD_TITLE = u'首页'

MALE = 'male'
FEMALE = 'female'

SEX = (
    (MALE, u'男'),
    (FEMALE, u'女'),
)

TRUE_FALSE = ((False, u'否'), (True, u'是'))

DICT_NULL_BLANK_TRUE = {
    'null': True,
    'blank': True
}


class ReadStatus(object):
    UNREAD = 0
    READ = 1
    DELETED = 99
    STATUS = (
        (UNREAD, u'未读'),
        (READ, u'已读'),
        (DELETED, u'删除'),
    )


class MailStatus(object):
    UNREAD = 0
    READ = 1
    DRAFT = 2
    TRASH = 3
    DELETED = 99
    STATUS = (
        (UNREAD, u'未读'),
        (READ, u'已读'),
        (DRAFT, u'草稿'),
        (TRASH, u'回收站'),
        (DELETED, u'删除'),
    )


class UsableStatus(object):
    UNUSABLE = 0
    USABLE = 1
    DELETED = 99
    STATUS = (
        (UNUSABLE, u'禁用'),
        (USABLE, u'启用'),
        (DELETED, u'删除'),
    )

class SutraStatus(object):
    UNREADY = 0
    READY = 1
    DONE = 3
    DELETED = 99
    STATUS = (
        (UNREADY, u'未准备好'),
        (READY, u'待校对'),
        (DONE, u'完成校对'),
        (DELETED, u'已删除'),
    )

class TaskStatus(object):
    NORMAL = 0
    FINISHED = 1
    EXCEPT = 2
    DELETED = 99
    TASK_STATUS = (
        (NORMAL, u'正常(进行中)'),
        (FINISHED, u'完成'),
        (EXCEPT, u'异常'),
        (DELETED, u'删除')
    )

class TaskType(object):
    VERIFY = 0
    COLLATE = 1

    TASK_TYPE = (
        (VERIFY, u'校对'),
        (COLLATE, u'校勘'),
    )

class Position(object):
    STAFF = 0
    MANAGE = 1
    INN_STAFF = 2
    MASTER = 3

    POSITIONS = (
        (STAFF, u'义工'),
        (MANAGE, u'义工组长'),
        (INN_STAFF, u'管理员'),
        (MASTER, u'部组法师'),
    )