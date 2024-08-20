from rest_framework import serializers
from .models import Triples

class TriplesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Triples
        fields = '__all__'