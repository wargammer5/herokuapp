from rest_framework import serializers
from .models import TypeDonaite

class TypeDonaiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDonaite
        fields = ('name', 'number_user')