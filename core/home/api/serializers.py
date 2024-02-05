from rest_framework import serializers
from home.models import Contribution


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ['user', 'donor_name', 'phone', 'email', 'address', 'people', 'requests']
