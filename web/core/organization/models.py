# coding=utf-8
from django.core.urlresolvers import reverse

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from core.adminlte import constants
from core.adminlte.constants import UsableStatus, DICT_NULL_BLANK_TRUE
from core.adminlte.models import BaseModel, User

from annoying.fields import AutoOneToOneField

class Organization(MPTTModel, BaseModel, UsableStatus):
    name = models.CharField(
        max_length=200, unique=True, verbose_name=u'组织名称'
    )
    parent = TreeForeignKey(
        'self', verbose_name=u'上级组织',
        related_name='organization_children',
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        u'状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE
    )

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = u'组织'

    class Config:
        list_display_fields = ('name', 'parent', 'id')
        list_form_fields = list_display_fields


class Department(MPTTModel, BaseModel, UsableStatus):
    organization = models.ForeignKey(
        Organization,
        verbose_name='所属组织',
        related_name='departments',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    name = models.CharField(
        max_length=50, unique=True, verbose_name=u'部门名称'
    )
    parent = TreeForeignKey(
        'self',
        related_name='department_children',
        verbose_name=u'上级部门',
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        u'状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE
    )

    class Meta:
        verbose_name_plural = verbose_name = u'部门'

    class MPTTMeta:
        order_insertion_by = ['name']

    class Config:
        list_display_fields = (
            'organization', 'parent', 'name', 'id'
        )
        list_form_fields = list_display_fields

    def __unicode__(self):
        return u'/%s/%s' % (self.organization.name, self.name)

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )


class AbstractPersonInfo(BaseModel, UsableStatus):
    VALID = 1
    INVALID = 2
    STAFF_STATUS = (
        (VALID, u'有效'),
        (INVALID, u'无效'),
    )
    real_name = models.CharField(
        verbose_name=u'真实姓名', max_length=20
    )
    sex = models.CharField(
        verbose_name=u'性别', max_length=10, choices=constants.SEX
    )
    cellphone = models.CharField(
        verbose_name=u'手机', max_length=11,  **DICT_NULL_BLANK_TRUE
    )
    birthday = models.DateField(
        verbose_name=u'生日', **DICT_NULL_BLANK_TRUE
    )
    qq = models.CharField(
        verbose_name=u'QQ', max_length=20, **DICT_NULL_BLANK_TRUE
    )
    email = models.EmailField(
        verbose_name=u'邮箱', max_length=100, **DICT_NULL_BLANK_TRUE
    )
    location = models.CharField(
        verbose_name=u'地址', max_length=200, **DICT_NULL_BLANK_TRUE
    )
    avatar = models.ImageField(
        upload_to='adminlte/user_avatar',
        default='adminlte/user_avatar/xianer02.jpg',
        **DICT_NULL_BLANK_TRUE
    )
    job_status = models.IntegerField(
        verbose_name=u'状态',
        choices=STAFF_STATUS,
        default=VALID
    )
    status = models.PositiveSmallIntegerField(
        u'数据状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE
    )
    position = models.PositiveSmallIntegerField(
        verbose_name=u'职位',
        choices=constants.Position.POSITIONS,
        default=constants.Position.STAFF,
        **DICT_NULL_BLANK_TRUE
    )

    class Meta:
        abstract = True


class Staff(AbstractPersonInfo):
    user = AutoOneToOneField(
        User, verbose_name=u'登录账号', related_name='staff_of'
    )
    department = models.ForeignKey(
        Department, verbose_name=u'所在小组', default=1
    )

    prefer_task_id = models.IntegerField(
        u'首选任务ID', default=0)

    def __unicode__(self):
        return u'%s/%s' % (self.department, self.real_name)

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = u'义工'

    class Config:
        list_display_fields = (
            'user', 'real_name', 'department', 'cellphone',
            'status', 'position', 'id'
        )
        list_form_fields = list_display_fields + ('avatar', )


# class UserProfile(models.Model):
# user = models.OneToOneField(User, verbose_name=u'用户')
# avatar = models.ImageField(verbose_name=u'头像', null=True, blank=False,
# upload_to='adminlte/user_avatar')
#
# class Meta:
# verbose_name_plural = verbose_name = u'用户资料'
#
# class Config:
# list_display_fields = ('user', 'id')
# list_form_fields = ('user', 'avatar', 'id')
#
#         @classmethod
#         def filter_queryset(cls, request, queryset):
#             return queryset.exclude(
#                 user=User.objects.filter(
#                     is_superuser=True, is_active=True
#                 ).first()
#             )
