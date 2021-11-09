from rest_framework import serializers
from .models import FormDonaite

class HebronOneHundredSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormDonaite
        fields = ('id', 'coat', 'way_of_writing', 'pib','email')