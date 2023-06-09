from django.db import models

# Create your models here.

class Invitacion(models.Model):
    invitado  = models.CharField(max_length = 255, blank = True, null = True)
    
    class Meta:
        verbose_name_plural = "invitaciones"
        
    def __str__(self):
        return str(self.invitado)