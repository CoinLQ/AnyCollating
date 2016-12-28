# coding=utf-8
from rest_framework import serializers
from .models import Task, Notification, SiteMailReceive, SiteMailSend
from core.catalogue.models import LQSutra, Reel



class SiteMailReceiveSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username')
    status = serializers.SerializerMethodField()
    status_value = serializers.IntegerField(source='status')
    sender_avatar = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    def get_sender_avatar(self, obj):
        return obj.sender.staff_of.avatar.url

    class Meta:
        model = SiteMailReceive
        fields = SiteMailReceive.Config.list_display_fields + (
            'sender_avatar', 'status_value'
        )
        read_only_fields = (
            'id', 'send_time', 'sender_avatar', 'status_value'
        )


class SiteMailSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMailSend
        fields = SiteMailSend.Config.list_display_fields
        read_only_fields = (
            'id', 'send_time'
        )


class NotificationSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source='content.contents')
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Notification
        fields = (
            'id', 'title', 'content', 'status', 'send_time', 'read_time',
            'creator', 'created_at'
        )
        read_only_fields = (
            'id', 'created_at'
        )



class ContentObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `tagged_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """
        if isinstance(value, LQSutra):
            return 'LQSutra: ' + value.__unicode__()
        elif isinstance(value, Reel):
            return 'Real: ' + value.__unicode__()
        raise Exception('Unexpected type of tagged object')


class TaskSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    content_object = ContentObjectRelatedField(read_only=True)
    def get_percent(self, obj):
        return '%s%%' % obj.percent

    def get_status(self, obj):
        return obj.get_status_display()

    def get_task_status(self, obj):
        return obj.get_task_status_display()

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'percent', 'status', 'task_type',
            'start_time', 'end_time',
            'creator', 'created_at', 'content_object', 'content_type'
        )
        read_only_fields = (
            'id', 'created_at', 'status'
        )
