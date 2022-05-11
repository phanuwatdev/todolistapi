from urllib import request
from rest_framework import serializers
from .models import Todolist

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ['created_date','id','task','checked','order']
    
class TodoSerializer(serializers.Serializer):
    created_date = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    task = serializers.CharField(required=False, allow_blank=True, max_length=200)
    checked = serializers.BooleanField(required=False)
    order = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        """
        Create and return a new `Todo` instance, given the validated data.
        """
        return Todolist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todolist` instance, given the validated data.
        """
        instance.task = validated_data.get('task', instance.task)
        instance.checked = validated_data.get('checked', instance.checked)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance

class TodoUpdateALlSerializer(serializers.Serializer):
    created_date = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    task = serializers.CharField(required=False, allow_blank=True, max_length=200)
    checked = serializers.BooleanField(required=False)
    order = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        """
        Create and return a new `Todo` instance, given the validated data.
        """
        return Todolist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todolist` instance, given the validated data.
        """
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.id = validated_data.get('id', instance.id)
        instance.task = validated_data.get('task', instance.task)
        instance.checked = validated_data.get('checked', instance.checked)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance


class TodoCheckedSerializer(serializers.Serializer):
    created_date = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    task = serializers.CharField(required=False, allow_blank=True, max_length=200)
    checked = serializers.BooleanField(required=False)
    order = serializers.IntegerField(required=False, allow_null=True)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todolist` instance, given the validated data.
        """
        instance.checked = validated_data.get('checked', instance.checked)
        instance.save()
        return instance
