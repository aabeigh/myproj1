from django.shortcuts import render
from django.http import HttpResponse
import logging
import boto3
from botocore.exceptions import ClientError


# Create your views here.
def myfunction1(request):
    return HttpResponse("<h1> My First DjangoApp</h1>")

def myfunction2(request):
    return HttpResponse("<h2> This is second function</h2>")
def testboto(request):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        return HttpResponse(f'  {bucket["Name"]}')


