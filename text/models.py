from django.db import models
from user.models import Admin

class Texts(models.Model):
    text = models.TextField()
    created_by = models.TextField(default="")
    created_at = models.DateField(auto_now_add=True, null=True)
    json_created = models.JSONField(default=dict)
    
    def body(self):
        return {
            'id' : self.id,
            'text' : self.text,
            'created_by' : self.created_by,
            'created_at' : self.created_at,
            'json_created' : self.json_created,
        }
    
    class Meta:
        verbose_name = 'Text'

# class Graph(models.Model):
#     text = models.ForeignKey(Texts, on_delete=models.CASCADE, null = False)



#     def body(self):
#         return {
#             'id': self.id,
#             'text': self.text.body(),
            
#         }
