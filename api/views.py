from django.shortcuts import render


from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from api.serializers import CategoryS, SubcategoryS, ProductS
from api.models import Category, SubCategory, Product

@api_view(['GET'])
def categories(request):
    return JsonResponse(CategoryS(Category.objects.all(), many=True).data, safe=False)

