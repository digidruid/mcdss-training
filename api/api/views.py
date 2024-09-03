from rest_framework import generics
from .models import Agenda, AgendaItem
from .serializers import AgendaSerializer, AgendaItemSerializer

class AgendaItemList(generics.ListCreateAPIView):
    serializer_class = AgendaItemSerializer

    def get_queryset(self):
        queryset = AgendaItem.objects.all() 

        agendaId = self.request.query_params.get('agenda')
        if agendaId is not None:
            queryset = queryset.filter(agenda=agendaId)

        return queryset

class AgendaItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AgendaItemSerializer    
    queryset = AgendaItem.objects.all()

class AgendaList(generics.ListCreateAPIView):
    serializer_class = AgendaSerializer

    def get_queryset(self):
        queryset = Agenda.objects.all() 
        return queryset

class AgendaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AgendaSerializer    
    queryset = Agenda.objects.all()