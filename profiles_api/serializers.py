from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our API view"""
    name = serializers.CharField(max_length=10)
    '''Similar to forms you define a serializer and specify the fields that you want to accept in
    your serializer input. We create a field called 'name' and this value can be passed into 
    the request that will be validated by the serializer. Serializer also take care of validation rules
    for example charfield length, or data type'''


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        """Configure serializer to a specific model in our project"""
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {  # keys are specific fields that you want to custom configure
            'password': {
                'write_only': True,  # can not be retrieved using GET
                'style': {'input_type': 'password'}  # see only dots when entering password
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        # When we create a new object with our UserProfileSerializer it will validate the fields
        # provided to the serializer and pass it in create function passing in validated data.
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)