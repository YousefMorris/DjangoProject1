from rest_framework import serializers
from ecommerceapp.models import *
from rest_framework.validators import UniqueValidator
class Productseralizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(validators=[UniqueValidator(queryset=Product.objects.all())],max_length=100)
    image=serializers.ImageField()
    price=serializers.IntegerField()
    createdat = serializers.DateTimeField(read_only=True)
    updatedat = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data) 
        # pro=Product()
        # pro.name=validated_data['name']
        # pro.save()
        # return pro
    
    def update(self, instance, validated_data):
        #return super().update(instance, validated_data)
        return instance.update(**validated_data)