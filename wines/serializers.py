from rest_framework import serializers
from wines.models import Wine


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'