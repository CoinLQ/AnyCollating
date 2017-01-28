# -*- coding: utf-8 -*-
import xlrd
from django.core.cache import cache
from django.db import models
from django.db.models import Avg, Count, Q
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRelation
from core.messageset.models import Task
from core.adminlte.constants import DICT_NULL_BLANK_TRUE, TRUE_FALSE, SutraStatus
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.db import transaction

# Create your models here.
class Tripitaka(models.Model):
    name = models.CharField(u'名称', max_length=64)
    code = models.CharField(u'编码', max_length=4, unique=True)
    era = models.CharField(u'年代', max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name_plural = verbose_name = u'经藏'

    class Config:
        list_display_fields = ('name', 'code', 'era', 'id')
        list_form_fields = list_display_fields
        search_fields = list_display_fields

    @classmethod
    #@transaction.atomic
    def import_from_xls(cls, input_file):
        book = xlrd.open_workbook(filename=None, file_contents=input_file.read())
        sh = book.sheet_by_index(0)
        # validate header
        error_messages = []
        for rl in range(sh.ncols):
            verbose_fields = map(lambda x: x.verbose_name, cls._meta.fields)
            if sh.cell_value(rowx=0, colx=rl) not in verbose_fields:
                error_msg = u"{0} doesn't exist in table".format(sh.cell_value(rowx=0, colx=rl))
                return False, error_msg
        for rx in range(1, sh.nrows):
            if not sh.cell_value(rowx=rx, colx=0):
                try:
                    t = cls(name=sh.cell_value(rowx=rx, colx=1), code=sh.cell_value(rowx=rx, colx=2), era=sh.cell_value(rowx=rx, colx=3))
                    t.save()
                except Exception, e:
                    error_messages.append(u'第{0}行: {1}'.format(rx + 1, e.message))
        if error_messages:
            return False, '<br/>'.join(error_messages[:10])
        else:
            return True, 'OK'

class VariantTripitaka(models.Model):
    tripitaka = models.ForeignKey(Tripitaka, null=False, related_name='variants', verbose_name = u'经藏')
    code = models.CharField(u'编码', max_length=6, unique=True)
    vendor = models.CharField(u'出版商', max_length=64)
    pub_date = models.DateField(u'出版日期')
    pub_version = models.CharField(u'版本批次', max_length=32)
    display = models.CharField(u'名称', max_length=64)

    cover = models.ImageField(u'封面信息', upload_to = 'cover', **DICT_NULL_BLANK_TRUE)
    volumes_count = models.SmallIntegerField(u'总册数', default=1)

    is_electronic = models.BooleanField(u'是否为电子版', choices=TRUE_FALSE, default=False)

    def __unicode__(self):
        return self.display

    class Meta:
        ordering = ('id',)
        verbose_name_plural = verbose_name = u'实体经藏'

    class Config:
        list_display_fields = ('display', 'tripitaka', 'code', 'vendor', 'pub_version', 'pub_date', 'is_electronic', 'volumes_count', 'id')
        list_form_fields = ('display', 'tripitaka', 'code', 'vendor', 'pub_version', 'pub_date', 'cover', 'is_electronic', 'volumes_count', 'id')
        search_fields = list_display_fields

    @classmethod
    #@transaction.atomic
    def import_from_xls(cls, input_file):
        book = xlrd.open_workbook(filename=None, file_contents=input_file.read())
        sh = book.sheet_by_index(0)
        # validate header
        error_messages = []
        for rl in range(sh.ncols):
            verbose_fields = map(lambda x: x.verbose_name, cls._meta.fields)
            if sh.cell_value(rowx=0, colx=rl) not in verbose_fields:
                error_msg = u"{0} doesn't exist in table".format(sh.cell_value(rowx=0, colx=rl))
                return False, error_msg
        for rx in range(1, sh.nrows):
            if not sh.cell_value(rowx=rx, colx=0):
                try:
                    t = cls(tripitaka_id=int(sh.cell_value(rowx=rx, colx=1)),
                            code=sh.cell_value(rowx=rx, colx=2),
                            vendor=sh.cell_value(rowx=rx, colx=3),
                            pub_date=xlrd.xldate.xldate_as_datetime(sh.cell_value(rowx=rx, colx=4), 0).strftime("%Y-%m-%d"),
                            pub_version=sh.cell_value(rowx=rx, colx=5),
                            display=sh.cell_value(rowx=rx, colx=6),
                            volumes_count=sh.cell_value(rowx=rx, colx=8))
                    t.save()
                except Exception, e:
                    error_messages.append(u'第{0}行: {1}'.format(rx + 1, e.message))
        if error_messages:
            return False, '<br/>'.join(error_messages[:10])
        else:
            return True, 'OK'

class Volume(models.Model):
    tripitaka = models.ForeignKey(VariantTripitaka, null=False, related_name='volumes', verbose_name = u'经藏')
    code = models.CharField(u'编码', max_length=12, default='')
    vol_num = models.SmallIntegerField(u'册序号', default=1)

    pages_count = models.SmallIntegerField(u'总页数', default=0)
    start_page = models.SmallIntegerField(u'起始页码', default=1)
    end_page = models.SmallIntegerField(u'终止页码', default=1)

    @classmethod
    def format_volume(cls, tripitaka, number):
        return '{0}-V{1:04}'.format(tripitaka.code, number)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = verbose_name = u'册'

    def __unicode__(self):
        return u'%s %s' % (self.tripitaka.display, self.vol_num)

    class Config:
        list_display_fields = ('tripitaka', 'code', 'vol_num', 'pages_count', 'start_page', 'end_page', 'id')
        list_form_fields = ('tripitaka', 'vol_num', 'pages_count', 'start_page', 'end_page', 'id')
        search_fields = list_display_fields

    @classmethod
    #@transaction.atomic
    def import_from_xls(cls, input_file):
        book = xlrd.open_workbook(filename=None, file_contents=input_file.read())
        sh = book.sheet_by_index(0)
        # validate header
        error_messages = []
        for rl in range(sh.ncols):
            verbose_fields = map(lambda x: x.verbose_name, cls._meta.fields)
            if sh.cell_value(rowx=0, colx=rl) not in verbose_fields:
                error_msg = u"{0} doesn't exist in table".format(sh.cell_value(rowx=0, colx=rl))
                return False, error_msg
        for rx in range(1, sh.nrows):
            if not sh.cell_value(rowx=rx, colx=0):
                try:
                    t = cls(tripitaka_id=sh.cell_value(rowx=rx, colx=1),
                            vol_num=int(sh.cell_value(rowx=rx, colx=3)),
                            pages_count=sh.cell_value(rowx=rx, colx=4),
                            start_page=sh.cell_value(rowx=rx, colx=5),
                            end_page=sh.cell_value(rowx=rx, colx=6))
                    t.save()
                except Exception, e:
                    error_messages.append(u'第{0}行: {1}'.format(rx + 1, e.message))
        if error_messages:
            return False, '<br/>'.join(error_messages[:10])
        else:
            return True, 'OK'

@receiver(pre_save, sender=Volume)
def pre_save_volume(sender, instance, **kwargs):
    if instance.pk is not None:
        pass
    else:
        instance.code = 'V{0:04}'.format(instance.vol_num)

@python_2_unicode_compatible
class LQSutra(models.Model):
    code = models.CharField(u'编码', max_length=6, default='')
    name = models.CharField(u'名称', max_length=128, default='')
    translator = models.CharField(u'译者', max_length=32, default='')
    reels_count = models.SmallIntegerField(u'总卷数', default=1)
    is_opened = models.BooleanField(u'是否可校勘', choices=TRUE_FALSE, default=False)

    tasks = GenericRelation(Task, related_query_name='tasks')

    def __str__(self):
        return '%s-%s' % (self.name, self.translator)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = verbose_name = u'龙泉经目'

    class Config:
        list_display_fields = ('name', 'translator', 'code', 'reels_count',  'is_opened', 'id')
        list_form_fields = list_display_fields
        search_fields = list_display_fields

    @classmethod
    #@transaction.atomic
    def import_from_xls(cls, input_file):
        book = xlrd.open_workbook(filename=None, file_contents=input_file.read())
        sh = book.sheet_by_index(0)
        # validate header
        error_messages = []
        for rl in range(sh.ncols):
            verbose_fields = map(lambda x: x.verbose_name, cls._meta.fields)
            if sh.cell_value(rowx=0, colx=rl) not in verbose_fields:
                error_msg = u"{0} doesn't exist in table".format(sh.cell_value(rowx=0, colx=rl))
                return False, error_msg
        for rx in range(1, sh.nrows):
            if not sh.cell_value(rowx=rx, colx=0):
                try:
                    t = cls(code='{0:05}'.format(int(sh.cell_value(rowx=rx, colx=1))),
                            name=sh.cell_value(rowx=rx, colx=2),
                            translator=sh.cell_value(rowx=rx, colx=3),
                            reels_count=sh.cell_value(rowx=rx, colx=4))
                    t.save()
                except Exception, e:
                    error_messages.append(u'第{0}行: {1}'.format(rx + 1, e.message))
        if error_messages:
            return False, '<br/>'.join(error_messages[:10])
        else:
            return True, 'OK'

class Sutra(models.Model):
    code = models.CharField(u'编码', max_length=16, default='', unique=True)
    tripitaka = models.ForeignKey(VariantTripitaka, null=False, related_name='sutras', verbose_name = u'经藏')
    normal_sutra = models.ForeignKey(LQSutra, related_name='sutras', null=False, verbose_name = u'龙泉经目')
    display = models.CharField(u'经本名称', max_length=128, default='')
    era = models.CharField(u'年代', max_length=12, default='')
    author = models.CharField(u'作者', max_length=32, default='', **DICT_NULL_BLANK_TRUE)
    translator = models.CharField(u'译者', max_length=32, default='', **DICT_NULL_BLANK_TRUE)
    # 译经之前的原始卷数
    reels_count = models.SmallIntegerField(u'总卷数', default=1)

    start_vol = models.SmallIntegerField(u'起始册码', default=0)
    start_page = models.SmallIntegerField(u'起始页码', default=0)
    end_vol = models.SmallIntegerField(u'终止册码', default=0)
    end_page = models.SmallIntegerField(u'终止页码', default=0)
    discription = models.CharField(u'描述信息', max_length=512, default='', **DICT_NULL_BLANK_TRUE)

    status = models.SmallIntegerField(u'校对状态', choices=SutraStatus.STATUS, default=SutraStatus.UNREADY)

    def __unicode__(self):
        return '%s-%s' % (self.display, self.tripitaka.display)

    class Meta:
        verbose_name_plural = verbose_name = u'实体经本'

    class Config:
        app_label = "catalogue"
        list_display_fields = ('normal_sutra', 'code', 'display', 'tripitaka', 'era', 'reels_count',  'start_vol', 'start_page', 'end_vol', 'end_page', 'id')
        list_form_fields = ('normal_sutra', 'display', 'tripitaka', 'era', 'reels_count', 'id',
                            'author', 'translator', 'start_vol', 'start_page', 'end_vol', 'end_page', 'discription')

    @staticmethod
    def retrieve_reel_by_index(sutra_code, index):
        reel_code = '{0}-R{1:03}'.format(sutra_code, index)
        reel = Reel.objects.filter(code=reel_code).first()
        return model_to_dict(reel)

    @classmethod
    #@transaction.atomic
    def import_from_xls(cls, input_file):
        book = xlrd.open_workbook(filename=None, file_contents=input_file.read())
        sh = book.sheet_by_index(0)
        # validate header
        error_messages = []
        for rl in range(sh.ncols):
            verbose_fields = map(lambda x: x.verbose_name, cls._meta.fields)
            if sh.cell_value(rowx=0, colx=rl) not in verbose_fields:
                error_msg = u"{0} doesn't exist in table".format(sh.cell_value(rowx=0, colx=rl))
                return False, error_msg
        for rx in range(1, sh.nrows):
            if not sh.cell_value(rowx=rx, colx=0):
                try:
                    t = cls(tripitaka_id=int(sh.cell_value(rowx=rx, colx=2)),
                            normal_sutra_id=int(sh.cell_value(rowx=rx, colx=3)),
                            display=sh.cell_value(rowx=rx, colx=4),
                            era=sh.cell_value(rowx=rx, colx=5),
                            author=sh.cell_value(rowx=rx, colx=6),
                            translator=sh.cell_value(rowx=rx, colx=7),
                            reels_count=sh.cell_value(rowx=rx, colx=8),
                            start_vol=int(sh.cell_value(rowx=rx, colx=9)),
                            start_page=int(sh.cell_value(rowx=rx, colx=10)),
                            end_vol=int(sh.cell_value(rowx=rx, colx=11)),
                            end_page=int(sh.cell_value(rowx=rx, colx=12)),
                            discription=sh.cell_value(rowx=rx, colx=13)
                            )
                    t.save()
                except Exception, e:
                    error_messages.append(u'第{0}行: {1}'.format(rx + 1, e.message))
        if error_messages:
            return False, '<br/>'.join(error_messages[:10])
        else:
            return True, 'OK'

@receiver(pre_save, sender=Sutra)
def pre_save_sutra(sender, instance, **kwargs):
    if instance.pk is not None:
        pass
    else:
        instance.code = '%sS%s' % (instance.tripitaka.code, instance.normal_sutra.code)
    # initial image size info


# juan (ancient mode)
class Reel(models.Model):
    sutra = models.ForeignKey(Sutra, null=False, related_name='reels', verbose_name = u'实体经本')
    reel_num = models.SmallIntegerField(u'卷序号', default=1)
    code = models.CharField(u'编码', max_length=16, default='', unique=True)
    start_vol = models.SmallIntegerField(u'起始册码', default=0)
    start_page = models.SmallIntegerField(u'起始页码', default=0)
    end_vol = models.SmallIntegerField(u'终止册码', default=0)
    end_page = models.SmallIntegerField(u'终止页码', default=0)
    text_content_trad = models.TextField(u'卷文本（繁体）', default='', **DICT_NULL_BLANK_TRUE)
    text_content_simpl = models.TextField(u'卷文本（简体）', default='', **DICT_NULL_BLANK_TRUE)

    status = models.SmallIntegerField(u'校对状态', choices=SutraStatus.STATUS, default=SutraStatus.READY)

    def __unicode__(self):
        return u'%s 第%s卷' % (self.sutra.__unicode__(), self.reel_num)

    class Meta:
        verbose_name_plural = verbose_name = u'卷信息'

    class Config:
        app_label = "catalogue"
        list_display_fields = ('sutra', 'reel_num', 'code', 'text_content_trad',  'start_vol', 'start_page', 'end_vol', 'end_page', 'id')
        list_form_fields = ('sutra', 'reel_num', 'text_content_trad',  'start_vol', 'start_page', 'end_vol', 'end_page', 'id')

    def begin_page_code(self):
        return '{0}V{1:04}P{2:04}'.format(self.sutra.code, self.start_vol, self.start_page)

    def end_page_code(self):
        return '{0}V{1:04}P{2:04}'.format(self.sutra.code, self.end_vol, self.end_page)

    def page_counts(self):
        return self.pages.count()

    @classmethod
    #@transaction.atomic
    def import_from_xls(cls, input_file):
        book = xlrd.open_workbook(filename=None, file_contents=input_file.read())
        sh = book.sheet_by_index(0)
        # validate header
        error_messages = []
        for rl in range(sh.ncols):
            verbose_fields = map(lambda x: x.verbose_name, cls._meta.fields)
            if sh.cell_value(rowx=0, colx=rl) not in verbose_fields:
                error_msg = u"{0} doesn't exist in table".format(sh.cell_value(rowx=0, colx=rl))
                return False, error_msg
        for rx in range(1, sh.nrows):
            if not sh.cell_value(rowx=rx, colx=0):
                try:
                    t = cls(sutra_id=int(sh.cell_value(rowx=rx, colx=1)),
                            reel_num=int(sh.cell_value(rowx=rx, colx=2)),
                            start_vol=int(sh.cell_value(rowx=rx, colx=4)),
                            start_page=int(sh.cell_value(rowx=rx, colx=5)),
                            end_vol=int(sh.cell_value(rowx=rx, colx=6)),
                            end_page=int(sh.cell_value(rowx=rx, colx=7)),
                            text_content_trad=sh.cell_value(rowx=rx, colx=8)
                            )
                    t.save()
                except Exception, e:
                    error_messages.append(u'第{0}行: {1}'.format(rx + 1, e.message))
        if error_messages:
            return False, '<br/>'.join(error_messages[:10])
        else:
            return True, 'OK'

@receiver(pre_save, sender=Reel)
def pre_save_reel(sender, instance, **kwargs):
    if instance.pk is not None:
        pass
    else:
        instance.code = '{0}-R{1:03}'.format(instance.sutra.code, instance.reel_num)

class Page(models.Model):
    reel = models.ForeignKey(Reel, related_name='pages', null=True, verbose_name = u'所属卷')
    volume = models.ForeignKey(Volume, related_name='pages', null=True, verbose_name = u'所属册')
    sutra = models.ForeignKey(Sutra, related_name='pages', null=True, verbose_name = u'实体经本')
    code = models.CharField(u'编码', max_length=20, default='', unique=True, null=True, blank=True)
    page_num = models.SmallIntegerField(u'序号', default=1)
    text_content_trad = models.TextField(u'页文本（繁体）', default='', **DICT_NULL_BLANK_TRUE)
    text_content_simpl = models.TextField(u'页文本（简体）', default='', **DICT_NULL_BLANK_TRUE)

    status = models.SmallIntegerField(u'校对状态', choices=SutraStatus.STATUS, default=SutraStatus.READY)

    class Meta:
        verbose_name_plural = verbose_name = u'页信息'

    class Config:
        list_display_fields = ('reel', 'volume', 'code', 'text_content_trad',  'page_num', 'id')
        list_form_fields = ('reel', 'volume', 'sutra', 'text_content_trad',  'page_num', 'id')

    def get_image_path(self):
        return "/data/share/dzj_characters/page_images/{0}/{1}/{2:04}.jpg".format(self.sutra.code[0:4], self.code[6:10], self.page_num)

    @property
    def image_url(self):
        return "/page_images/{0}/{1}.jpg".format(self.code[0:4], self.code)

@receiver(pre_save, sender=Page)
def pre_save_page(sender, instance, **kwargs):
    if instance.pk is not None:
        pass
    else:
        instance.code = '{0}{1}P{2:04}'.format(instance.sutra.code, instance.volume.code, instance.page_num)

