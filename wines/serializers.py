from rest_framework import serializers
from wines.models import Wine


class WineSerializer(serializers.ModelSerializer):

    bottle_price = serializers.SerializerMethodField()

    class Meta:
        model = Wine
        fields = '__all__'

    def get_bottle_price(self, obj):
        total = obj.case_price / obj.case_size
        total = round(total, 2)
        return total