from rest_framework import serializers


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(write_only=True, allow_blank=False)
    password = serializers.CharField(max_length=16, min_length=8, write_only=True, allow_blank=False)

    def update(self, instance, validated_data):
        return None

    def create(self, validated_data):
        return None
