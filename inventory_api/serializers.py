from rest_framework import serializers
from inventory_api.models import *
from drf_writable_nested import UniqueFieldsMixin

class LocationSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    location_id = serializers.IntegerField(required=False)
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

class EanDeviceSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    ean_device_id = serializers.IntegerField(required=False)
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

class DeviceSerializer(serializers.ModelSerializer):
    device_id = serializers.IntegerField(required=False)
    ean_device = EanDeviceSerializer()
    location = LocationSerializer()
    class Meta:
        model = DeviceModel
        fields = ['device_id', 'name', 'serial_number', 'description', 'ean_device', 'location', 'quantity', 'condition', 'status', 'date_added', 'qr_code', 'returned']
        extra_kwargs = {
            'serial_number': {'required': True},
            'ean_device': {'required': True},
            'location': {'required': True},
            'quantity': {'required': True},
            'condition': {'required': True},
            'status': {'required': True},
            'qr_code': {'required': True},
        }

    def create(self, validated_data):
        ean_device = validated_data.pop("ean_device")
        location = validated_data.pop("location")

        try:
            ean_device = EanDeviceModel.objects.get(ean_device_id=ean_device.get('ean_device_id', None))
        except EanDeviceModel.DoesNotExist:
            raise serializers.ValidationError("Invalid ean_device_id")
        try:
            location = LocationModel.objects.get(location_id=location.get('location_id', None))
        except LocationModel.DoesNotExist:
            raise serializers.ValidationError("Invalid location_id")
        device = DeviceModel.objects.create(ean_device=ean_device, location=location, **validated_data)
        return device

    def update(self, instance, validated_data):
        ean_device = validated_data.pop("ean_device")
        location = validated_data.pop("location")

        try:
            new_ean_device = EanDeviceModel.objects.get(ean_device_id=ean_device.get('ean_device_id', None))
        except EanDeviceModel.DoesNotExist:
            raise serializers.ValidationError("Invalid ean_device_id")
        try:
            new_location = LocationModel.objects.get(location_id=location.get('location_id', None))
        except LocationModel.DoesNotExist:
            raise serializers.ValidationError("Invalid location_id")

        instance.name = validated_data.get('name', instance.name)
        instance.serial_number = validated_data.get('serial_number', instance.serial_number)
        instance.description = validated_data.get('description', instance.description)
        instance.ean_device = new_ean_device
        instance.location = new_location
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.condition = validated_data.get('condition', instance.condition)
        instance.status = validated_data.get('status', instance.status)
        instance.date_added = instance.date_added
        instance.qr_code = validated_data.get('qr_code', instance.qr_code)
        instance.returned = validated_data.get('returned', instance.returned)

        return super().update(instance, validated_data)

class DeviceHistorySerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    class Meta:
        model = DeviceHistoryModel
        fields = ['history_id', 'event', 'device', 'date']
        extra_kwargs = {
            'device': {'required': True},
        }

    def create(self, validated_data):
        del validated_data['history_id']
        history = DeviceHistoryModel.objects.create(**validated_data)
        return history