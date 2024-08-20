from django.db import models

class Triples(models.Model):
    entity1 = models.TextField()
    relationship = models.TextField()
    entity2 = models.TextField()
    text = models.TextField()
    
    def body(self):
        return {
            'id' : self.id,
            'entity1' : self.entity1,
            'relationship' : self.relationship,
            'entity2' : self.entity2,
        }
    
    class Meta:
        verbose_name = 'Triples'