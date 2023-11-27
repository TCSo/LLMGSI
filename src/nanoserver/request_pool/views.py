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

class InferView(views.APIView):
    def post(self, request, endpoint_name, format=None):
        response = {}
        try:
            with transaction.atomic():
                llm_request = LLMRequest(
                    input_data = {'input': request.data.get('input','Please introduce yourself as a teaching assistent in UC Berkeley.')},
                )
                llm_request.save()
                code = llm_request.code
                print('Request No.', code, 'Received !!!')
                print(llm_request.input_data)

        except Exception as e:
            raise APIException(str(e))
        try:
            answer = query_response(llm_request.input_data.get('input'))
            response['data'] = str(answer)
            response['succeed'] = 1
            print('LLMGSI:', str(answer))
            llm_request.response_data = response['data']
            llm_request.succeed = True
            llm_request.save()
        except:
            llm_request.succeed = False
            response['succeed'] = 0
            llm_request.save()

        return Response(response)