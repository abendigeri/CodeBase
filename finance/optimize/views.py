# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


import json

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from optimize.models import Investment
from optimize.serializers import InvestmentSerializer

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import linearoptimization


class InvestmentList(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    name = 'investment-list'


class InvestmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    name = 'investment-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'investment': reverse(InvestmentList.name,
                                  request=request)
        })


@csrf_exempt
@api_view(['GET', 'POST'])
def investment_list(request):
    if request.method == 'POST':

        # print(type(request.data))
        # x = request.data

        linearoptimization.getInvestments(
            total_amount=1000000000, data=request.data)

        # print(x)
        # print(x["constraints"]["commitments"])
        return Response(request.data, status=status.HTTP_201_CREATED)
