from rest_framework import serializers
from optimize.models import Investment


class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
    # Display all the details for the related drone

    # investments = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='investment-detail')

    class Meta:
        model = Investment
        fields = (
            'url',
            'pk',
            'name',
            'returns',
            'risk')
