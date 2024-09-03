from django.urls import path
from .views import AgendaList, AgendaDetail, AgendaItemList, AgendaItemDetail 

urlpatterns = [
    path('agendas/', AgendaList.as_view()),
    path('agendas/<int:pk>/', AgendaDetail.as_view()),
    path('agendas/items/', AgendaItemList.as_view()),
    path('agendas/items/<int:pk>/', AgendaItemList.as_view()),
]