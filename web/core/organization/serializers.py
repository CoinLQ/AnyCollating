# coding=utf-8
from rest_framework import serializers
from .models import Organization, Department, Staff




class OrganizationSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    def get_parent(self, obj):
        return obj.parent.name if obj.parent else '-'

    class Meta:
        model = Organization
        fields = (
            'id', 'name', 'parent'
        )


class DepartmentSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(source='organization.name')
    parent = serializers.SerializerMethodField()

    def get_parent(self, obj):
        return obj.parent.name if obj.parent else '-'

    class Meta:
        model = Department
        fields = (
            'id', 'organization', 'name', 'parent'
        )


class StaffSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_department(self, obj):
        return u'[%s]%s' % (obj.department.organization.name, obj.department.name)

    def get_status(self, obj):
        return obj.get_status_display()

    def get_position(self, obj):
        return obj.get_position_display()

    class Meta:
        model = Staff
        fields = Staff.Config.list_display_fields
        read_only_fields = (
            'id', 'user', 'status'
        )