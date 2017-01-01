# coding=utf-8
import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from core.adminlte.constants import ReadStatus, TaskStatus, MailStatus, \
    UsableStatus, TaskType, \
    DICT_NULL_BLANK_TRUE
from core.adminlte.models import BaseModel



class AbstractMessageContent(BaseModel, UsableStatus):
    title = models.CharField(
        verbose_name=u'标题', max_length=200
    )
    contents = models.TextField(
        verbose_name=u'内容'
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=u'状态',
        choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE,
        db_index=True
    )

    class Meta:
        abstract = True


class SiteMailContent(AbstractMessageContent):
    receivers = models.ManyToManyField(
        User, blank=True,
        related_name='sitemail_receivers',
        verbose_name=u'接收人',
        help_text=u'不选则发送给全体用户'
    )

    class Meta:
        verbose_name_plural = verbose_name = u'站内邮件内容'

    def __unicode__(self):
        return self.title

    class Config:
        success_url = reverse_lazy(
            'adminlte:common_list_page',
            kwargs={
                'app_name': 'messageset',
                'model_name': 'sitemailreceive'
            }
        )
        list_form_fields = (
            'title', 'contents', 'receivers'
        )


class AbstractSiteMail(BaseModel, MailStatus):
    title = models.CharField(
        verbose_name=u'主题',
        max_length=200
    )
    content = models.ForeignKey(
        SiteMailContent,
        verbose_name=u'内容'
    )
    sender = models.ForeignKey(
        User,
        related_name='+',
        verbose_name=u'发件人',
        **DICT_NULL_BLANK_TRUE
    )
    send_time = models.DateTimeField(
        verbose_name=u'发送时间',
        auto_now_add=True,
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=u'读取状态',
        choices=MailStatus.STATUS,
        default=MailStatus.UNREAD,
        db_index=True
    )

    class Meta:
        abstract = True


class SiteMailSend(AbstractSiteMail):
    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name_plural = verbose_name = u'发件箱'

    class Config:
        detail_template_name = 'messageset/sitemail_detail.html'
        list_display_fields = (
            'title', 'send_time', 'id'
        )
        list_form_fields = (
            'title',
            'content.contents',
            'send_time',
        )
        filter_fields = ('status', )
        search_fields = ('title', )

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.filter(sender=request.user).exclude(
                status=SiteMailSend.DELETED
            )


class SiteMailReceive(AbstractSiteMail):
    receive = models.ForeignKey(
        User,
        related_name='+',
        verbose_name=u'收件人',
        **DICT_NULL_BLANK_TRUE
    )
    read_time = models.DateTimeField(
        verbose_name=u'读取时间',
        **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name_plural = verbose_name = u'收件箱'

    class Config:
        list_template_name = 'messageset/sitemail_list.html'
        form_template_name = 'messageset/sitemail_form.html'
        detail_template_name = 'messageset/sitemail_detail.html'
        list_display_fields = (
            'title', 'sender',
            'status', 'send_time', 'id'
        )
        list_form_fields = (
            'title', 'sender', 'content.contents'
        )
        filter_fields = ('status', )
        search_fields = ('title', )

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.filter(receive=request.user).exclude(
                status=SiteMailReceive.DELETED
            )
            # if 'receive' in request.query_params \
            # or 'trash' in request.query_params:
            # receive = request.query_params.get('receive', None)
            #     if receive:
            #
            #     trash = request.query_params.get('trash', None)
            #     if trash:
            #         queryset = queryset.filter(
            #             Q(status=SiteMailReceive.DELETED),
            #             Q(sender=request.user) | Q(receive=request.user)
            #         )
            # else:
            #     queryset = SiteMailReceive.objects.none()
            # return queryset

        @classmethod
        def get_object_hook(cls, request, obj):
            save_flag = False
            if obj.status != ReadStatus.READ:
                obj.status = ReadStatus.READ
                save_flag = True
            if not obj.read_time:
                obj.read_time = datetime.datetime.now()
                save_flag = True
            if save_flag:
                obj.save()


class NotificationContent(AbstractMessageContent):
    receivers = models.ManyToManyField(
        User, blank=True,
        related_name='notification_receivers',
        verbose_name=u'接收人',
        help_text=u'不选则发送给全体用户'
    )

    class Meta:
        verbose_name_plural = verbose_name = u'系统通知内容'

    def __unicode__(self):
        return self.title

    class Config:
        success_url = reverse_lazy(
            'adminlte:common_list_page',
            kwargs={
                'app_name': 'messageset',
                'model_name': 'notification'
            }
        )
        list_form_fields = (
            'title', 'contents', 'receivers'
        )


class Notification(BaseModel, ReadStatus):
    title = models.CharField(
        verbose_name=u'标题',
        max_length=200,
        default='',
        **DICT_NULL_BLANK_TRUE
    )
    content = models.ForeignKey(
        NotificationContent,
        verbose_name=u'内容',
        **DICT_NULL_BLANK_TRUE
    )
    receive = models.ForeignKey(
        User,
        related_name='+',
        verbose_name=u'接收人',
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=u'读取状态',
        choices=ReadStatus.STATUS,
        default=ReadStatus.UNREAD,
        db_index=True
    )
    send_time = models.DateTimeField(
        verbose_name=u'发送时间',
        auto_now_add=True,
        **DICT_NULL_BLANK_TRUE
    )
    read_time = models.DateTimeField(
        verbose_name=u'读取时间',
        **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return u'%s' % self.content.title

    class Meta:
        verbose_name_plural = verbose_name = u'系统通知'

    class Config:
        list_template_name = 'messageset/notification_list.html'
        list_display_fields = (
            'title', 'status', 'send_time', 'id'
        )
        list_form_fields = (
            'title', 'content.contents', 'send_time'
        )
        filter_fields = ('status',)
        search_fields = ('title',)

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.exclude(status=Notification.DELETED).filter(
                receive=request.user
            )

        @classmethod
        def get_object_hook(cls, request, obj):
            obj.status = ReadStatus.READ
            if not obj.read_time:
                obj.read_time = datetime.datetime.now()
            obj.save()


class Task(BaseModel, TaskStatus):
    name = models.CharField(
        verbose_name=u'任务名称', max_length=200
    )
    percent = models.PositiveIntegerField(
        verbose_name=u'进度', default=0
    )

    pos = models.PositiveIntegerField(
        verbose_name=u'位置', default=0
    )

    status = models.PositiveSmallIntegerField(
        verbose_name=u'状态',
        choices=TaskStatus.TASK_STATUS,
        default=TaskStatus.NORMAL,
        db_index=True
    )

    task_type = models.PositiveSmallIntegerField(
        verbose_name=u'类型',
        choices=TaskType.TASK_TYPE,
        default=TaskType.VERIFY,
        db_index=True
    )
    start_time = models.DateTimeField(
        verbose_name=u'开始时间', auto_now_add=True, **DICT_NULL_BLANK_TRUE
    )
    end_time = models.DateTimeField(
        verbose_name=u'结束时间', **DICT_NULL_BLANK_TRUE
    )
    limit = models.Q(app_label='catalogue', model='reel')
    content_type = models.ForeignKey(ContentType, limit_choices_to=limit, on_delete=models.CASCADE, **DICT_NULL_BLANK_TRUE)
    object_id = models.PositiveIntegerField(**DICT_NULL_BLANK_TRUE)
    content_object = GenericForeignKey('content_type', 'object_id')

    def goto_next_page(self):
        model_clz = ContentType.objects.get(app_label='catalogue', model='page').model_class()
        page_code = self.next_page_code()
        page = model_clz.objects.filter(code=page_code).first()

        if page is None:
            vol_num = int(page_code.split("P")[-2].split("V")[-1]) + 1
            new_page_code = '{0}V{1:04}P{2:04}'.format(self.content_object.sutra.code, vol_num, 1)
            page = model_clz.objects.filter(code=new_page_code).first()

        return page

    def get_current_page_image(self):
        model_clz = ContentType.objects.get(app_label='catalogue', model='page').model_class()
        if self.current_page_code is None:
            self.current_page_code = '{0}V{1:04}P{2:04}'.format(self.content_object.sutra.code, self.content_object.start_vol, self.content_object.start_page)
            self.save()
        page = model_clz.objects.filter(code=self.current_page_code).first()
        return page.image_url

    def page_counts(self):
        return self.content_object.pages.count()

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

    def build_pages(self):
        for page in self.content_object.pages.all():
            task_page = TaskPage(task=self, code=page.code, page=page, status=0)
            task_page.save()

    def update_percent(self):
        self.percent = int(self.task_pages.filter(status=1).count()*100/self.task_pages.count())
        if (self.percent == 100):
            self.status = TaskStatus.EXCEPT
        self.save()

    @property
    def task_pages(self):
        return self.task_pages.order_by('id')

    @property
    def reel(self):
        return self.content_object

    class Meta:
        verbose_name_plural = verbose_name = u'个人任务'

    class Config:
        # 列表页模板
        list_template_name = 'messageset/task_list.html'
        detail_template_name = 'messageset/task_detail.html'
        # 列表页展现的字段
        list_display_fields = (
            'name', 'percent', 'task_type', 'status',
            'start_time', 'end_time', 'content_object', 'id'
        )
        # 表单页需要填写的字段
        list_form_fields = (
            'creator', 'name', 'percent', 'task_type', 'status', 'content_type', 'object_id'
        )
        # 数据过滤
        filter_fields = ('status', )
        # 模糊搜索
        search_fields = ('name', 'task_type')

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.filter(creator=request.user).exclude(
                status=TaskStatus.DELETED
            )


class TaskPage(BaseModel):
    from core.catalogue.models import Page
    task = models.ForeignKey(Task, related_name='task_pages', null=True, verbose_name = u'所属任务')
    code = models.CharField(u'编码', max_length=20, default='', db_index=True, null=True, blank=True)
    page = models.ForeignKey(Page, related_name='content_pages', null=True, verbose_name = u'所属页面')
    text_content_trad = models.TextField(u'页文本（繁体）', default='', **DICT_NULL_BLANK_TRUE)
    status = models.PositiveSmallIntegerField(
        verbose_name=u'状态',
        choices=UsableStatus.STATUS,
        default=0,

    )

@receiver(m2m_changed, sender=SiteMailContent.receivers.through)
def create_sitemail_datas(sender, instance, **kwargs):
    """
    发送邮件时，向收件箱和发件箱添加数据，
    这里将来可以替换为异步消息队列
    :param sender:
    :param instance:
    :param kwargs:
    """
    kwargs = {
        'title': instance.title,
        'content': instance,
        'sender': instance.creator,
        'creator': instance.creator
    }
    SiteMailSend(**kwargs).save()
    for user in instance.receivers.all():
        tmp_kwargs = {
            'receive': user,
        }
        tmp_kwargs.update(kwargs)
        SiteMailReceive(**tmp_kwargs).save()


@receiver(m2m_changed, sender=NotificationContent.receivers.through)
def create_notification_datas(sender, instance, **kwargs):
    """
    保存系统通知时，给所选用户发送通知，
    目前是向Notification表添加数据
    这里将来可以替换为异步消息队列
    :param sender:
    :param instance:
    :param kwargs:
    """
    for user in instance.receivers.all():
        exists = Notification.objects.filter(
            receive=user, content=instance
        ).exists()
        if not exists:
            nf = Notification()
            nf.title = instance.title
            nf.content = instance
            nf.receive = user
            nf.creator = instance.creator
            nf.status = Notification.UNREAD
            nf.save()
