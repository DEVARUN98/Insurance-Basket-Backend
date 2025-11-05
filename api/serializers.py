from rest_framework import serializers
from companies.models import Companies


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = "__all__"


