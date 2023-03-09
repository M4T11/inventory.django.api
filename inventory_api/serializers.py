from rest_framework import serializers
from inventory_api.models import *
from drf_writable_nested import UniqueFieldsMixin

class LocationSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ['location_id', 'name']
        extra_kwargs = {
            'name': {'required': True},
        }

class ProducerSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    producer_id = serializers.IntegerField(required=False)
    class Meta:
        model = ProducerModel
        fields = ['producer_id', 'name']
        extra_kwargs = {
            'name': {'required': True},
        }

class CategorySerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    category_id = serializers.IntegerField(required=False)
    class Meta:
        model = CategoryModel
        fields = ['category_id', 'name']
        extra_kwargs = {
            'name': {'required': True},
        }

class EanDeviceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    producer = ProducerSerializer()
    class Meta:
        model = EanDeviceModel
        fields = ['ean_device_id', 'ean', 'category', 'producer', 'model']
        extra_kwargs = {
            'ean': {'required': True},
            'category': {'required': True},
            'producer': {'required': True},
            'model': {'required': True},
        }

    def create(self, validated_data):
        category = validated_data.pop("category")
        producer = validated_data.pop("producer")
        try:
            category = CategoryModel.objects.get(category_id=category.get('category_id', None))
        except CategoryModel.DoesNotExist:
            raise serializers.ValidationError("Invalid category_id")
        try:
            producer = ProducerModel.objects.get(producer_id=producer.get('producer_id', None))
        except ProducerModel.DoesNotExist:
            raise serializers.ValidationError("Invalid producer_id")

        ean_device = EanDeviceModel.objects.create(category=category, producer=producer, **validated_data)
        return ean_device

    def update(self, instance, validated_data):
        category = validated_data.pop("category")
        producer = validated_data.pop("producer")
        instance.ean = validated_data.get('ean', instance.ean)
        try:
            instance.category = CategoryModel.objects.get(category_id=category.get('category_id', None))
        except CategoryModel.DoesNotExist:
            raise serializers.ValidationError("Invalid category_id")
        try:
            instance.producer = ProducerModel.objects.get(producer_id=producer.get('producer_id', None))
        except ProducerModel.DoesNotExist:
            raise serializers.ValidationError("Invalid producer_id")

        instance.model = validated_data.get('model', instance.model)
        return super().update(instance, validated_data)