from django.db import models
from django import forms
from django.utils import timezone
from datetime import datetime

# Create your models here.
class FileInfo(models.Model):
    name = models.CharField(max_length=255, default='')
    created_by = models.TextField(default="")
    created_at = models.DateField(auto_now_add=True, null=True)
    time = models.DateTimeField(default=datetime.now)
    json_created = models.JSONField(default=dict)

    def body(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'created_by' : self.created_by,
            'created_at' : self.created_at,
            'time': self.time,
            'json_created' : self.json_created,
        }
    
    class Meta:
        verbose_name = 'File'

class UploadFile(models.Model):
    file = models.FileField(upload_to='upload', null = True)
    file_text = models.TextField(default='', null = True)
    info = models.ForeignKey(FileInfo, on_delete=models.CASCADE, null = True)
    
    def body(self):
        return {
            'id' : self.id,
            'file_text' : self.file_text,
            'info' : self.info.body(),
            'file_url' : 'http://localhost:8000' + self.file.url
        }
