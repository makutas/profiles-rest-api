from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our API view"""
    name = serializers.CharField(max_length=10)
    '''Similar to forms you define a serializer and specify the fields that you want to accept in
    your serializer input. We create a field called 'name' and this value can be passed into 
    the request that will be validated by the serializer. Serializer also take care of validation rules
    for example charfield length, or data type'''
