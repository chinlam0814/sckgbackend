from rest_framework import serializers
from .models import UploadFile, FileInfo

class FileInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = '__all__'

class UploadFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = '__all__'