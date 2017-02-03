# coding=utf-8
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from core.adminlte.constants import TaskStatus, MailStatus, \
    UsableStatus, TaskType, \
    DICT_NULL_BLANK_TRUE
from core.adminlte.models import BaseModel

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

    @staticmethod
    def accept_verify_task(user, reel):
        task = Task(creator=user, content_object=reel, name=u'校对'+reel.__unicode__())
        task.save()
        task.build_pages()
        return task

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
        self.save()

    def owned_by(self, user):
        if self.creator == user:
            return True
        else:
            return False

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