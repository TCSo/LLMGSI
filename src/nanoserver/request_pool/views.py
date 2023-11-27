from django.shortcuts import render
from request_engine import *
import json
import os

import time, shutil
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (generics, mixins, permissions, status, views,
                            viewsets)
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .models import LLMRequest
# Create your views here.

response = query_response(question)

class InferView(views.APIView):
    def post(self, request, endpoint_name, format=None):
        response = {}
        try:
            with transaction.atomic():
                llm_request = LLMRequest(
                    input_data = request.data,
                )
                llm_request.save()
                code = llm_request.code
                print('Request No.', code, 'Received !!!')
        except Exception as e:
            raise APIException(str(e))
        try:
            answer = query_response(request.data.values())
            response['data'] = answer
            llm_request.response_data = response
            llm_request.succeed = True
            llm_request.save()
        except:
            llm_request.succeed = False
            llm_request.save()

        return Response(response)