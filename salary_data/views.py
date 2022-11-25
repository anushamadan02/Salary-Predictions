from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from salary_data.models import salary_data
from salary_data.serializers import  SalaryDataSerializer


#for executing the python script which in turn executes the sql script
from django.http import HttpResponse
from django.views.generic import View
import subprocess

#is_valid checks if the data is valid and is in the right format
@csrf_exempt
def salaryDataApi(request,Id=0):
    if request.method=='GET':
        salaryDetails = salary_data.objects.all()
        salaryDetails_serializer=SalaryDataSerializer(salaryDetails,many=True)   
        return JsonResponse(salaryDetails_serializer.data,safe=False)
    elif request.method=='POST':
        salarydetail_data=JSONParser().parse(request)
        salaryDetails_serializer=SalaryDataSerializer(data=salarydetail_data, many=True)
        if salaryDetails_serializer.is_valid():
            salaryDetails_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        salarydetail_data=JSONParser().parse(request)
        salarydetail=salary_data.objects.get(Id=salarydetail_data['Id'])
        salaryDetails_serializer=SalaryDataSerializer(salarydetail,data=salarydetail_data)
        if salaryDetails_serializer.is_valid():
            salaryDetails_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        salarydetail=salary_data.objects.get(Id=Id)
        salarydetail.delete()
        return JsonResponse("Deleted Successfully",safe=False)

def error_404_view(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'Resource not found',
        # 'message': exception
    })

def error_500_view(request, exception=None):
    return JsonResponse({
        'status_code': 500,
        'error': 'Internal Server Error',
        # 'message': exception
    })

def error_400_view(request, exception=None):
    return JsonResponse({
        'status_code': 400,
        'error': 'Bad Request',
        # 'message': exception
    })