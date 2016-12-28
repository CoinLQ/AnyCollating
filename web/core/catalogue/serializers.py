# coding=utf-8
from rest_framework import serializers
from .models import Sutra, Tripitaka, VariantTripitaka, Volume, LQSutra, Reel, Page

class SutraSerializer(serializers.ModelSerializer):
    tripitaka = serializers.StringRelatedField(many=False)
    normal_sutra = serializers.StringRelatedField(many=False)
    class Meta:
        model = Sutra
        fields = Sutra.Config.list_display_fields
        read_only_fields = ('name', 'code')


class TripitakaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tripitaka
        fields = Tripitaka.Config.list_display_fields
        read_only_fields = ('code')

class VariantTripitakaSerializer(serializers.ModelSerializer):
    tripitaka = serializers.StringRelatedField(many=False)
    class Meta:
        model = VariantTripitaka
        fields = VariantTripitaka.Config.list_display_fields
        read_only_fields = ('code')

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = Volume.Config.list_display_fields
        read_only_fields = ('code')

class LQSutraSerializer(serializers.ModelSerializer):
    class Meta:
        model = LQSutra
        fields = LQSutra.Config.list_display_fields
        read_only_fields = ('code')

class ReelSerializer(serializers.ModelSerializer):
    sutra = serializers.StringRelatedField(many=False)
    class Meta:
        model = Reel
        fields = Reel.Config.list_display_fields
        read_only_fields = ('code')

class PageSerializer(serializers.ModelSerializer):
    reel = serializers.StringRelatedField(many=False)
    volume = serializers.StringRelatedField(many=False)
    class Meta:
        model = Page
        fields = Page.Config.list_display_fields
        read_only_fields = ('code')