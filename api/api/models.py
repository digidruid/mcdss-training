from django.db import models

# Create your models here.
class Agenda(models.Model):
    dayId = models.IntegerField(unique=True)
    agendaTitle = models.CharField(max_length=64)
    completed = models.BooleanField()

    def __str__(self):
        return 'Day %i: %s' % (self.dayId,self.agendaTitle)

class AgendaItem(models.Model):

    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    itemId = models.IntegerField() # for ordering the items
    itemDesc = models.CharField(max_length=255)
    itemURL = models.CharField(max_length=1024)
    completed = models.BooleanField()

    def __str__(self):
        return "%i: %s" % (self.itemId,self.itemDesc)



    