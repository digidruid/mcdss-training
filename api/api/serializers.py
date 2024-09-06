from rest_framework import serializers
from .models import Agenda, AgendaItem


class AgendaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaItem
        fields = ('__all__')

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('__all__')

