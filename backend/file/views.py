from django.shortcuts import render
from django.http import JsonResponse
from .models import UploadFile, FileInfo
import json
import PyPDF2

# Create your views here.

def returnJson(data=None, pageCount=0, errorCode=0):
	if data is None:
		data = []
	return JsonResponse({'errorCode': errorCode, 'data': data})

def files_list(request):
	files = UploadFile.objects.all()
	return returnJson([dict(file.body()) for file in files])


def file_info(requst, pk):
	try:
		file_info = FileInfo.objects.get(id=pk)
	except FileInfo.DoesNotExist:
		return returnJson([], 0, 404)
	
	return returnJson([dict(file_info.body())])

def file(reqeust, pk):
	try:
		file_info = FileInfo.objects.get(id=pk)
	
	except FileInfo.DoesNotExist:
		return returnJson([], 0, 404)
	
	file = UploadFile.objects.filter(file_info=file_info).first()

	if file is None:
		return returnJson()
	
	return returnJson([dict(file.body())])

def create_file_info(request):
	data = json.loads(request.body)

	try:
		files_info = FileInfo.objects.get(name=data['name'])
	
	except FileInfo.DoesNotExist:
		file_info = FileInfo.objects.create(name=data['name'], created_by=data['username'], json_created=data['json_created'])
		file_info.save()

		return returnJson([dict(file_info.body())])
	
	return returnJson([], 0, 404)

def create_file(request, pk):
	try:
		file_info = FileInfo.objects.get(id=pk)
	except FileInfo.DoesNotExist:
		return returnJson([], 0, 404)
	
	# text = extract_text_from_pdf(request.FILES.get('file'))
	file = UploadFile.objects.create(info=file_info, file=request.FILES.get('file'))

	return returnJson([dict(file.body())])

def delete_file(request, pk):
	file_info = FileInfo.objects.get(id=pk)

	if request.method == 'DELETE':
			file_info.delete()
			files = UploadFile.objects.all()
			return returnJson([dict(file.body()) for file in files])

def extract_text_from_pdf(request):
    file = request.FILES.get('file')
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return returnJson([text])