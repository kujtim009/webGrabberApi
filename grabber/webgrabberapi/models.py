from django.db import models

class Reshtat(models.Model):
    emri = models.CharField(db_index=True, max_length=5)
    
    def __str__(self):
        return self.emri